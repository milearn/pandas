import pandas as pd
# import numpy as np
# import yfinance as yf
# import datetime as dt
# from pandas_datareader import data as pdr


df = pd.read_csv('data.csv')

print('showing just top 2 rows')
print(df.head(2))


print('showing just last 2 rows')
print(df.tail(2))

print('data types for series')
print(df.dtypes)

print('writing to file')
print(df.to_excel('names.xlsx', sheet_name="passangers", index=False))

print('printing size of data frame')
print(df.shape) # (8,9)
print(df.info()) # get general info about data frames, like column names, data type for each column
print(df.describe()) # stats info like count, mean , min, max
print(df["Name"].shape) #(8,) -> because its a 1D series

print(df["Ticket"] > 10)
print(df["Ticket"] > 10)

print(df[df["Ticket"]>10]) # boolean key inside []. filters the data

print(df[(df["PassengerId"] == 2) | (df["PassengerId"] == 3)]) # can't use or and here.


# Using loc or iloc
# df[bool] -> This will only filter out the rows
# df.loc[condition, condition] -> Can filter both rows and columns
print('Get names of passengers with Ticket greater than 10')
print(df.loc[df["Ticket"] >10, "Name"])

# filter rows and column by index
print(df.iloc[3:5, 2:5])