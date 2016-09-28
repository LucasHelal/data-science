# Now we'll learn about arithmetic between DataFrames with different indexes
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# Lets start by making two Series

ser1 = Series([0, 1, 2], index=['A', 'B', 'C'])

# Now second Series 2
ser2 = Series([3, 4, 5, 6], index=['A', 'B', 'C', 'D'])

# So what happens when we add these together
ser1 + ser2
# Note the NaN values are added in automatically

# Now let's try it with DataFrames!
dframe1 = DataFrame(np.arange(4).reshape(
    2, 2), columns=list('AB'), index=['NYC', 'LA'])


# Second DataFrame
dframe2 = DataFrame(np.arange(9).reshape(
    3, 3), columns=list('ADC'), index=['NYC', 'SF', 'LA'])

# What happens when we add them together?
dframe1 + dframe2

# What if we want to replace the NaN values
# Then we can use .add()
dframe1.add(dframe2, fill_value=0)

# Now we can see that the values are filled, however there was no SF,
# B value so that is still NaN
# Lets learn about operations betwen a Series and a DataFrame

# Create a Series from DataFrame's 0 row
ser3 = dframe2.ix[0]

# Now we can use arithmetic operations
dframe2 - ser3
