import numpy as np
# Create array
arr = np.arange(50).reshape((10, 5))

# Lets transpose
arr.T

# Taking dot product of matrices
np.dot(arr.T, arr)

# For 3D matrix
arr3d = np.arange(50).reshape((5, 5, 2))

# We can also transpose a 3d matrix
arr3d.transpose((1, 0, 2))

# If you need to get more specific use swapaxes
arr = np.array([[1, 2, 3]])

arr.swapaxes(0, 1)
