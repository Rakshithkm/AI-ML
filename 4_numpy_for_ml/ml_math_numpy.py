import numpy as np

# Feature matrix (X)
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5]
])

# Weights
w = np.array([0.5, 1.0])

# Linear model: y = Xw
y_pred = np.dot(X, w)
print("Predictions:", y_pred)
