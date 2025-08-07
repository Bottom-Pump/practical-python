# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    'Open a given portfolio file and read it into a list of tuples (name,shares,price)'
    with open(filename) as file:
        portfolio = parse_csv(file=file,
                              select=['name','shares','price'],
                              types=[str,int,float])
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portfolio]
    return portfolio

def read_prices(filename):
    ''' 
    read a set of prices into a dictionary 
    keys: stock names
    values: prices.
    '''
    with open(filename) as file:
        prices = parse_csv(file=file,
                    types=[str,float],
                    has_headers=False)
    prices = dict(prices)
    return prices
                
def make_report(portfolio,prices):
    '[portfolio]:list of the stock price you purchase \n [prices]: tuples of the current share price of the stock'
    report = []
    for stock in portfolio:
        name = stock.name
        shares = stock.shares
        price = prices[name]
        change = price - stock.price
        report.append((name,shares,price,change))
    return report

def print_report(reportdata,formatter):
    'Print a nicely formatted table from a list of (name, shares, price, change) tuples'
    headers = ('Name', 'Shares', 'Price', 'Change')
    # header
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # data
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)
    # print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    
def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)