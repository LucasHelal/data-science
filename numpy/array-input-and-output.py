import numpy as np

# Create an array
arr = np.arange(5)

# Saving array on disk in binary format (file extension .npy)
np.save('my_array', arr)

# Change arr
arr = np.arange(10)

# Lets see the original saved copy
np.load('my_array.npy')

# Saving multiple arrays into a zip file
np.savez('two_arrays.npz', x=arr, y=arr)

# Now loading multiple arrays
archive_array = np.load('two_arrays.npz')

# Show
archive_array['x']

# Now saving and loading text files
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('my_test_text.txt', arr, delimiter=',')

# Loading text files
arr = np.loadtxt('my_test_text.txt', delimiter=',')
