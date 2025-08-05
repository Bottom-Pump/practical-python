# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    'Open a given portfolio file and read it into a list of tuples (name,shares,price)'
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers  = next(rows)
        for rowno,row in enumerate(rows):
            record = dict(zip(headers,row))
            holding = {}
            try:
                holding['name'] = record['name']
                holding['shares'] = int(record['shares'])
                holding['price'] = float(record['price'])
            # This catches errors in int() and float() conversions above
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}')
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    ''' 
    read a set of prices into a dictionary 
    keys: stock names
    values: prices.
    '''
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        for rowno,row in enumerate(rows,start=2):
            try:
                prices[row[0]] = float(row[1])
            except Exception as e:
                print(f'Something get wrong in reading {filename}: row:{rowno}')
    return prices
                
def make_report(portfolio,prices):
    '[portfolio]:list of the stock price you purchase \n [prices]: tuples of the current share price of the stock'
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = prices[name]
        change = price - stock['price']
        report.append((name,shares,price,change))
    return report

def print_report(report):
    'print a formatted table'
    headers = ('Name', 'Shares', 'Price', 'Change')
    for i in headers:
        print('%10s' % i,end=' ')
    print()
    for i in headers:
        print('-'*10,end=' ')
    print()
    # data
    for name, shares, price, change in report:
        price_str = f"${price:.2f}"
        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)
    print_report(report)