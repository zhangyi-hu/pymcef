from __future__ import print_function

from datetime import datetime
from pandas_datareader import data
import pandas as pd

def get_close_prices(start, end, tickers):
    df = pd.DataFrame()
    for ticker in tickers:
        try:
            prices = data.DataReader(ticker, 'yahoo', start, end)['Close']
            if prices.index[0] == start:
                df[ticker] = prices
                print('\r' + ticker, end='')
        except:
            pass
    return df
