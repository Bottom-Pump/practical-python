# report.py
#
# Exercise 2.4
import csv

portfolio = []
prices = {}
report = []

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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as e:
                print(e)
    return prices
                
def make_report(portfolio,prices):
    '[portfolio]:list of the stock price you purchase \n [prices]: tuples of the current share price of the stock'
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = prices[name]
        change = price - stock['price']
        report.append((name,shares,price,change))
    # print a formatted table
    headers = ('Name', 'Shares', 'Price', 'Change')
    i = len(headers)
    while(i):
        print('%10s' % headers[len(headers) -i],end=' ')
        i -= 1
    print()
    i = len(headers)
    while(i):
        print('-'*10,end=' ')
        i -= 1
    print()
    # data
    for name, shares, price, change in report:
        price_str = f"${price:.2f}"
        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')
    return report

    