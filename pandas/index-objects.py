import numpy as np

from pandas import Series, DataFrame

import pandas as pd

# Let's learn/review about Index Objects
my_ser = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])

# Get the index
my_index = my_ser.index

# Can grab index ranges
my_index[2:]

# What happens if we try to change an index value?
my_index[0] = 'Z'
# ERROR!!  Indexes are immutable!
