import pandas as pd
# import numpy as np
# import yfinance as yf
# import datetime as dt
# from pandas_datareader import data as pdr


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)
print('------df-------\n')
print(df["Sex"])
print('filter 2 cols')
print(df["Age", "Sex"])
print('------Sex-------\n')

print('------df["Age"].max()-------\n')
print(df["Age"].max())

print('------df["Age"].describe()-------\n')
print(df["Age"].describe())


