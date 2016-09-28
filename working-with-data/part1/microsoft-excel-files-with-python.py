import pandas as pd

"""
IMPORTANT NOTE: NEED TO HAVE xlrd AND openpyxl INSTALLED!!!
"""

# Open the excel file as an object
xlsfile = pd.ExcelFile('Lec_28_test.xlsx')

# Parse the first sheet of the excel file and set as DataFrame
dframe = xlsfile.parse('Sheet1')
