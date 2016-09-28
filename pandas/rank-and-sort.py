import numpy as np
from numpy.random import randn
from pandas import Series, DataFrame
import pandas as pd

# Sorting by index
ser1 = Series(range(3), index=['C', 'A', 'B'])


# Now sort_index
ser1.sort_index()

# Can sort a Series by its values
ser1.order()

# Lets see how ranking works
ser2 = Series(randn(10))

# This will show you the rank used if you sort the series
ser2.rank()

# Lets sort it now
ser2.sort()

# After sorting let's check the rank and see iof it makes sense
ser2.rank()
# On the left column we see th original index value and on the right we
# see it's rank!
