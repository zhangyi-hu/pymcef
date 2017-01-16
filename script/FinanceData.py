from __future__ import print_function
from sys import stdout
from pandas_datareader import data
import pandas as pd

def get_close_prices(tickers, source, start, end):
    '''
    source: 'yahoo' or 'google'
    '''
    df = pd.DataFrame()
    n = len(tickers)
    for ticker, i in zip(tickers, range(n)):
        try:
            prices = data.DataReader(ticker, source, start, end)['Close']
            if prices.index[0] == start:
                df[ticker] = prices
                print('\r' + str(i*100/n) + '%', end='')
                stdout.flush()
        except:
            pass
    df = df[df > 5.0].dropna(axis=1) # remove penny stock
    return df.dropna(axis=1)
