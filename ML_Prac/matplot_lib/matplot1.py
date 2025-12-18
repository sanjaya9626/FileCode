import pandas as pd
import matplotlib.pyplot as plt

data_plot = pd.read_csv('output_csv_full.csv', index_col=0)

# print(data_plot.head())

# data_plot.plot()
# plt.show()

# I want to plot only the columns of the data table with the data from value.
# data_plot['value'].plot()
# plt.show()

#I want to visually compare the values measured in time_ref versus value
csv_data = pd.read_csv('overs_trade.csv')
# csv_data.plot.scatter(x=['Data_value'], y=['Period'], alpha=1)
# plt.show()

csv_data.plot.box()
# plt.show()

# I want each of the columns in a separate subplot.
csv_data.plot.area(figsize=(9, 2))
plt.show()

