import numpy as np
import webbrowser

# Universal functions perform operations on all elements in an array
arr = np.arange(11)

# Taking Square Roots
np.sqrt(arr)

# Calcualting exponential (e^)
np.exp(arr)

# Binary Functions require two arrays

# Random array (normal dist)
A = np.random.randn(10)

# Random array (normal dist)
B = np.random.randn(10)

# Addition
np.add(A, B)

# Finding max or min between two arrays
np.maximum(A, B)

# For full and extensive list of all universal functions
website = "http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
webbrowser.open(website)
