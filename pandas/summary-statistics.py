# Now we'll learn about pandas built-in methods of summarizing data founr
# in DataFrames
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

from IPython.display import YouTubeVideo

# Let's create a dataframe to work with
arr = np.array([[1, 2, np.nan], [np.nan, 3, 4]])
dframe1 = DataFrame(arr, index=['A', 'B'], columns=['One', 'Two', 'Three'])

# Let's see the sum() method in action
dframe1.sum()
# Notice how it ignores NaN values

# We can also over rows instead of columns
dframe1.sum(axis=1)

# Can also grab min and max values of dataframe
dframe1.min()

# As well as there index
dframe1.idxmin(
# Same deal with max, just replace min for max

# Can also do an accumulation sum
dframe1.cumsum()

# A very useful feature is describe, which provides summary statistics
dframe1.describe()

# We can also get information on correlation and covariance

# For more info on correlation and covariance, check out the videos below!

# For more information about Covariaance and Correlation
# Check out these great videos!
# Video credit: Brandon Foltz.

# CoVariance
YouTubeVideo('xGbpuFNR1ME')

# Correlation
YouTubeVideo('4EXNedimDMs')


# Now lets check correlation and covariance on some stock prices!

# Pandas can get info off the web
import pandas.io.data as pdweb

# Set datetime for date input
import datetime

# Get the closing prices

prices=pdweb.get_data_yahoo(['CVX', 'XOM', 'BP'],
                               start=datetime.datetime(2010, 1, 1),
                               end=datetime.datetime(2013, 1, 1))['Adj Close']
# Show preview
prices.head()

# Now lets get the volume trades

volume=pdweb.get_data_yahoo(['CVX', 'XOM', 'BP'],
                               start=datetime.datetime(2010, 1, 1),
                               end=datetime.datetime(2013, 1, 1))['Volume']

# Show preview
volume.head()

# Lets get the return
rets=prices.pct_change()

# Get the correlation of the stocks
corr=rets.corr

# Lets see the prices over time to get a very rough idea of the
# correlation between the stock prices
prices.plot()

import seaborn as sns
import matplotlib.pyplot as plt
% matplotlib inline

# As expected pretty strong correlations with eachother
sns.heatmap(rets.corr())

# We'll learn much more about seaborn later!


# We can also check for unique values and their counts

# For example
ser1=Series(['w', 'w', 'x', 'y', 'z', 'w', 'w', 'x', 'x', 'y', 'a', 'z'])

# Grab the unique values
ser1.unique()

# Now get the count of the unique values
ser1.value_counts()
