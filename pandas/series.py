from pandas import Series
import pandas as pd

# Lets create a Series (array of data and data labels, its index)
obj = Series([3, 6, 9, 12])

# Lets show the values
obj.values

# Lets show the index
obj.index

# Now lets create a Series with an index
# WW2 casualties
ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000], index=[
                 'USSR', 'Germany', 'China', 'Japan', 'USA'])

# Now we can use index values to select Series values
ww2_cas['USA']

# Can also check with array operations

# Check who had casualties greater than 4 million
ww2_cas[ww2_cas > 4000000]

# Can treat Series as ordered dictionary

# Check if USSR is in Series
'USSR' in ww2_cas

# Can convert Series into Python dictionary
ww2_dict = ww2_cas.to_dict()

# Can convert back into a Series
WW2_Series = Series(ww2_dict)

# Passing a dictionary the index will have the dict keys in order
countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']

# Lets redefine a Series
obj2 = Series(ww2_dict, index=countries)

# We can use isnull and notnull to find missing data
pd.isnull(obj2)
# obj2.isnull()

# Same for the opposite
pd.notnull(obj2)
# obj2.notnull()

# Now we can add and pandas automatically aligns data by index
WW2_Series + obj2

# We can give Series names
obj2.name = "World War 2 Casualties"

# We can also name index
obj2.index.name = 'Countries'
