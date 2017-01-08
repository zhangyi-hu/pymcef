from bs4 import BeautifulSoup
import requests
import pandas as pd

def _get_listed_table(url):
    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find(text='AAPL').parent.parent.parent
    return table

def get_listed_instruments(url):
    table = _get_listed_table(url)
    rows = table.find_all('tr')
    
    #strip column names
    colnames = [str(cell.string.strip()) for cell in rows[0].find_all('td')]
    
    df = pd.DataFrame(columns=colnames)
    
    i = 0
    for row in rows[1:]:
        cells = [cell.string for cell in row.find_all('td')]
        df.loc[i] = [None if cell is None else str(cell.strip()) for cell in cells]
        i += 1
    return df

def get_listed_symbols(url):
    table = _get_listed_table(url)
    rows = table.find_all('tr')
    
    #strip column names
    colnames = [str(cell.string.strip()) for cell in rows[0].find_all('td')]
    idx = colnames.index('Symbol')
    symbols = []
    for row in rows[1:]:
        symbol = str(row.find_all('td')[idx].string.strip())
        symbols.append(symbol)
    return symbols
