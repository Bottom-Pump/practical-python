# report.py
#
# Exercise 2.4
import csv

portfolio = []
prices = {}

def read_portfolio(filename):
    'Open a given portfolio file and read it into a list of tuples'
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers  = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    ''' 
    read a set of prices into a dictionary 
    keys: stock names
    values: prices.
    '''
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as e:
                print(e)
    return prices
                
    