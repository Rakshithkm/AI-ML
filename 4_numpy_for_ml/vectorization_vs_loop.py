import numpy as np
import time

# Using loop
numbers = list(range(1_000_000))

start = time.time()
squared_loop = []
for n in numbers:
    squared_loop.append(n ** 2)
print("Loop time:", time.time() - start)

# Using NumPy
arr = np.array(numbers)

start = time.time()
squared_np = arr ** 2
print("NumPy time:", time.time() - start)
print("First 5 squared values (loop):", squared_loop[:5])
print("First 5 squared values (NumPy):", squared_np[:5])