# Creating Numpy Arrays
import numpy as np

# Converting from a list
# Lets start with a list
my_list1 = [1, 2, 3, 4]

my_array1 = np.array(my_list1)

# Make another list
my_list2 = [11, 22, 33, 44]

# Make a list of lists
my_lists = [my_list1, my_list2]

# Make multi-dimensional array
my_array2 = np.array(my_lists)

# Lets get the size of the array
my_array2.shape

# Find out the data tyoe of the array
my_array2.dtype

# Making special case arrays

# Zeros
np.zeros(5)

# Ones
np.ones((5, 5))

# An empty array
np.empty(5)
np.empty((3, 4))

# Identity array
np.eye(5)

# Using a range
np.arange(5)
