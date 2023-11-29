from pandas_datareader import data, wb
import yfinance as yf
yf.pdr_override()

import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns

#starting and ending times for dates 
start= dt.datetime(2010,1,1)
end = dt.datetime(2023,1,1)
 
# Bank of America
BAC = data.get_data_yahoo('BAC', start, end)
 
# CitiGroup
C = data.get_data_yahoo('C', start, end)
 
# Goldman Sachs
GS = data.get_data_yahoo('GS', start, end)
 
# JPMorgan Chase
JPM = data.get_data_yahoo('JPM', start, end)
 
# Morgan Stanley
MS = data.get_data_yahoo('MS', start, end)
 
# Wells Fargo
WF = data.get_data_yahoo('WFC', start, end)

# list of ticker symbols in alphabetical order
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WF']

#joining together all bank stock dataframes along the columns and having the column heads be the tickers
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WF], axis = 1, keys = tickers)

#setting column name levels
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

#max closing price for each bank's stocks during time period
bank_stocks.xs(key = "Close", axis = 1, level = "Stock Info").max()

#creating dataFrame for stock returns
returns = pd.DataFrame()

for tick in tickers:
    returns[tick + " Returns"] = bank_stocks[tick]["Close"].pct_change()

# #pairplot to visualize data
# sns.pairplot(returns)

# #dates of banks with worst returns
returns.idxmin().head(5)

# #dates of banks with best returns
returns.idxmax().head(5)

#standard deviation of returns
returns.std()
#standrd deviation of returns in 2015
returns.loc['2015-01-01':'2015-12-31'].std()

# #distplot of Morgan Stanley returns in 2015
# sns.displot(returns.loc['2015-01-01':'2015-12-31']['MS Returns'])

