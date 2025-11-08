"""
environment.py
---------------
Generates random obstacles and defines the 3D space for path planning.
"""

import numpy as np

class Environment:
    def __init__(self, num_obstacles=5, space_limits=(0, 30)):
        self.num_obstacles = num_obstacles
        self.space_limits = space_limits
        self.obstacles = self.generate_random_obstacles()

    def generate_random_obstacles(self):
        low, high = self.space_limits
        return np.random.uniform(low, high, size=(self.num_obstacles, 3))

    def is_point_in_bounds(self, point):
        x, y, z = point
        low, high = self.space_limits
        return low <= x <= high and low <= y <= high and low <= z <= high

    def get_environment_summary(self):
        summary = f"🌍 Environment Bounds: {self.space_limits}\n"
        summary += f"🧱 Number of Obstacles: {self.num_obstacles}\n"
        summary += "🪨 Obstacle Coordinates (x, y, z):\n"
        for i, obs in enumerate(self.obstacles):
            summary += f"  {i+1}. {np.round(obs, 2)}\n"
        return summary
