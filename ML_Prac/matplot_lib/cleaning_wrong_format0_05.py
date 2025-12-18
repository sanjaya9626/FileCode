# data in a wrong format: to fix this problem, there are 2 ways:
# removing the rows or convert all the cells in the same format.

# loading and reading the original dataframe

import pandas as pd
df_val = pd.read_csv('year-past.csv')
# print(df_val.to_string())

#now lets try to convert all the cells in the
# date column into dates.via to datetime()

import pandas as pd
df_data = pd.read_csv('year-past.csv')
df_data['Date'] = pd.to_datetime(df_data['Date'], format='%m%d%Y', errors='coerce')
print(df_data.to_string())

#here now we will remove the rows with NULL
# value in the date column

# df_date_val = pd.read_csv('year-past.csv')
# df_date_val['Date'] = pd.to_datetime('Date')
# df_date_val.dropna(subset=['Date'], inplace =True)
# print(df_date_val.to_string())

