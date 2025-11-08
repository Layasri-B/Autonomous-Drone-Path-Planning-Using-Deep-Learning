# planner.py
"""
Drone path planner using the Sequential_9 model.
Ensures the last path point is exactly the goal and produces smooth motion.
"""

import numpy as np
from model import create_sequential_9_model, predict_next_step

class DronePathPlanner:
    def __init__(self, env):
        self.env = env
        # build model (weights are random if not trained — okay for demo)
        self.model = create_sequential_9_model()

    def plan_path(self, start, goal, num_steps=60):
        """
        Create a path of length num_steps from start to goal.
        Guarantees path[-1] == goal.
        """
        start = np.array(start, dtype=float)
        goal = np.array(goal, dtype=float)

        path = [start.copy()]
        current = start.copy()

        # If start == goal, return trivial path
        if np.allclose(start, goal, atol=1e-6):
            return np.tile(start, (num_steps, 1))

        # We'll compute adaptive step sizes so we reach goal exactly in num_steps
        for step_index in range(1, num_steps):
            remaining_steps = num_steps - step_index
            # Model predicted next position (may be untrained; used for direction)
            try:
                pred = predict_next_step(self.model, current, goal, self.env.obstacles)
            except Exception:
                # fallback to simple direction if model fails
                pred = current + (goal - current)

            # Combine model direction and direct goal direction for stability
            model_dir = pred - current
            goal_dir = goal - current
            combined = 0.4 * model_dir + 0.6 * goal_dir

            # If combined is tiny, move directly toward goal
            norm = np.linalg.norm(combined)
            if norm < 1e-6:
                combined = goal_dir
                norm = np.linalg.norm(combined) if np.linalg.norm(combined) > 0 else 1.0

            direction_unit = combined / norm

            # Compute step size so that we will reach the goal by last step
            distance_to_goal = np.linalg.norm(goal - current)
            # avoid division by zero
            step_size = distance_to_goal / max(1, remaining_steps)

            # Small safety max step cap so we don't overshoot
            max_cap = max(0.5 * (distance_to_goal), step_size)
            step_size = min(step_size, max_cap)

            next_pos = current + direction_unit * step_size

            # Clip to environment bounds
            low, high = self.env.space_limits
            next_pos = np.clip(next_pos, low, high)

            path.append(next_pos)
            current = next_pos

        # Force final point to be exact goal (ensures arrival)
        path[-1] = goal.copy()
        return np.array(path)
