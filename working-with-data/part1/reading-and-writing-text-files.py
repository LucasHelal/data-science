import sys
import pandas as pd

# Can open csv files as a dataframe
dframe = pd.read_csv('lec25.csv')

# Can also use read_table with ',' as a delimiter
dframe = pd.read_table('lec25.csv', sep=',')

# If we dont want the header to be the first row
dframe = pd.read_csv('lec25.csv', header=None)

# We can also indicate a particular number of rows to be read
pd.read_csv('lec25.csv', header=None, nrows=2)

# Now let's see how we can write DataFrames out to text files
dframe.to_csv('mytextdata_out.csv')

# You'll see this file where you're ipython Notebooks are saved (Usually
# under my documents)

#  We can also use other delimiters

# we'll import sys to see the output

# Use sys.stdout to see the output directly and not save it
dframe.to_csv(sys.stdout, sep='_')

# Just to make sure we understand the delimiter
dframe.to_csv(sys.stdout, sep='?')


# We can also choose to write only a specific subset of columns
dframe.to_csv(sys.stdout, columns=[0, 1, 2])

# You should also checkout pythons built-in csv reader and writer fot more info
# https://docs.python.org/2/library/csv.html
