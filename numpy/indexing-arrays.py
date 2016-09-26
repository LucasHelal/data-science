import numpy as np

# Creating sample array
arr = np.arange(0, 11)

# Get a value at an index
arr[8]

# Get values in a range
arr[1:5]

# Get values in a range
arr[0:5]

# Setting a value with index range (Broadcasting)
arr[0:5] = 100

# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0, 11)

# Important notes on Slices
slice_of_arr = arr[0:6]

# Show slice
slice_of_arr

# Now note the changes also occur in our original array!
arr

# Data is not copied, it's a view of the original array!
# This avoids memory problems
# To get a copy, need to be explicit
arr_copy = arr.copy()

# Indexing a 2D array
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))

# Indexing row
arr_2d[1]

# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
arr_2d[1][0]

# Shape bottom row
arr_2d[2]


# Shape bottom row
arr_2d[2, :]

# Fancy Indexing

# Set up matrix
arr2d = np.zeros((10, 10))

# Length of array
arr_length = arr2d.shape[1]

# Set up array
for i in range(arr_length):
    arr2d[i] = i

# Fancy indexing allows the following
arr2d[[2, 4, 6, 8]]

# Allows in any order
arr2d[[6, 4, 2, 7]]
