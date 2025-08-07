# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    'enter the portfolio to computer your total cost'
    portfolio = read_portfolio(filename)
    return sum(s.shares * s.price for s in portfolio)

def print_cost(filename):
    cost = portfolio_cost((filename))
    print('Total cost:', cost)

def main(argv):
    '''
        enter the portfolio to computer your total cost
        usage: python pcost.py portfolio.csv
    '''
    if len(argv) != 2:
        print('usage : python pcost.py portfolio.csv')
        
    filename = argv[1]
    print_cost(filename)
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
