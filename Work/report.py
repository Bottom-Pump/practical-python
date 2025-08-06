# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    'Open a given portfolio file and read it into a list of tuples (name,shares,price)'
    portfolio = parse_csv(filename=filename
                          ,select=['name','shares','price']
                          ,types=[str,int,float])
    
    return portfolio

def read_prices(filename):
    ''' 
    read a set of prices into a dictionary 
    keys: stock names
    values: prices.
    '''
    prices = parse_csv(filename=filename
                       ,types=[str,float]
                       ,has_headers=False)
    prices = dict(prices)
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
    
def main(argv):
    '''
        Process command-line parameters and generate reports
        usage: python report.py portfolio.csv prices.csv
    '''
    if len(argv) != 3:
        print('usage : python report.py portfolio.csv prices.csv')
        return 1
    
    portfolio_file = argv[1]
    prices_file = argv[2]
    portfolio_report(portfolio_file,prices_file)
    return 0
    
if __name__ == '__main__':
    import sys
    main(sys.argv)