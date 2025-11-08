"""
model.py
---------
Defines the Sequential_9 neural network model used for drone path planning.
This model predicts the next waypoint (x, y, z) based on current position,
goal position, and relative obstacle features.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
import numpy as np

def create_sequential_9_model(input_dim=9):
    """Create and return the Sequential_9 model."""
    model = Sequential(name="Sequential_9")
    model.add(Input(shape=(input_dim,)))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(3, activation='linear'))  # Predict next (x, y, z)
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model


def predict_next_step(model, current, goal, obstacles):
    """Predict the next step for the drone."""
    avg_obs = np.mean(obstacles, axis=0) if obstacles is not None and len(obstacles) > 0 else np.zeros(3)
    features = np.concatenate([current, goal, avg_obs]).reshape(1, -1)
    next_pos = model.predict(features, verbose=0)[0]
    return next_pos
# Example usage:
# model = create_sequential_9_model()   
