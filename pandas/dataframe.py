import numpy as np
import webbrowser
import pandas as pd
from pandas import Series, DataFrame

# Now we'll learn DataFrames

# Let's get some data to play with. How about the NFL?
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)

# Copy and read to get data
nfl_frame = pd.read_clipboard()

# We can grab the column names with .columns
nfl_frame.columns

# Lets see some specific data columns
DataFrame(nfl_frame, columns=['Team', 'First Season', 'Total Games'])

# What happens if we ask for a column that doesn't exist?
DataFrame(nfl_frame, columns=[
          'Team', 'First Season', 'Total Games', 'Stadium'])

# Call columns
nfl_frame.columns

# We can retrieve individual columns
nfl_frame.Team

# Or try this method for multiple word columns
nfl_frame['Total Games']

# We can retrieve rows through indexing
nfl_frame.ix[3]

# We can also assign value sto entire columns
nfl_frame['Stadium'] = "Levi's Stadium"  # Careful with the ' here

# Putting numbers for stadiums
nfl_frame["Stadium"] = np.arange(5)

# Call columns
nfl_frame.columns

# Adding a Series to a DataFrame
stadiums = Series(["Levi's Stadium", "AT&T Stadium"], index=[4, 0])


# Now input into the nfl DataFrame
nfl_frame['Stadium'] = stadiums

# We can also delete columns
del nfl_frame['Stadium']

# DataFrames can be constructed many ways. Another way is from a
# dictionary of equal length lists
data = {'City': ['SF', 'LA', 'NYC'],
        'Population': [837000, 3880000, 8400000]}

city_frame = DataFrame(data)

# For full list of ways to create DataFrames from various sources go to
# teh documentation for pandas:
website = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
webbrowser.open(website)
