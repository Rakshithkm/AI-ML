# Day 04 - NumPy Basics
# Author: Rakshith

import numpy as np

# Create arrays
data = np.array([10, 20, 30, 40, 50])
print("Data:", data)

# Shape
print("Shape:", data.shape)

# Basic operations
print("Mean:", np.mean(data))
print("Std:", np.std(data))

# Vectorized operation
scaled = data * 2
print("Scaled:", scaled)
