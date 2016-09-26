import numpy as np
from numpy.random import randn

import matplotlib.pyplot as plt
# Install Tkinter
# sudo apt-get install python3-tk

# Set array for one side of grid
points = np.arange(-5, 5, 0.01)

# Create the grid
dx, dy = np.meshgrid(points, points)

# Evaluating Function
z = (np.sin(dx) + np.sin(dy))

# Plot out the 2d array
plt.imshow(z)
# Plot with a colorbar
plt.colorbar()

# Give the plot a title
plt.title("Plot for sin(x)+sin(y)")

plt.waitforbuttonpress()
# #################################

# Lets learn how to use the numpy where

# First the slow way to do things
A = np.array([1, 2, 3, 4])

B = np.array([100, 200, 300, 400])

# Now a boolean array
condition = np.array([True, True, False, False])

# Using a list comprehension
answer = [(A_val if cond else B_val)
          for A_val, B_val, cond in zip(A, B, condition)]

# Problems include speed issues and multi-dimensional array issues
# Now using numpy.where
answer2 = np.where(condition, A, B)


# Can use np.where  on 2d for manipulation
arr = randn(5, 5)

# Where array is less than zero, make that value zero, otherwise leave it
# as the array value
np.where(arr < 0, 0, arr)

# Other Statistical Processing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# SUM
arr.sum()

# Can also do along an axis (we shold expect a 3 diff between the columns)
arr.sum(0)

# Mean
arr.mean()

# Standard Deviation
arr.std()

# Variance
arr.var()

# Also any and all for processing boolean arrays
bool_arr = np.array([True, False, True])

# For any True
bool_arr.any()

# For all True
bool_arr.all()

# Finally sort array

# Create a random array
arr = randn(5)

# Sort it
arr.sort()


# Lets learn about unique
countries = np.array(
    ['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])

np.unique(countries)

# in1d test values in one array
np.in1d(['France', 'USA', 'Sweden'], countries)
