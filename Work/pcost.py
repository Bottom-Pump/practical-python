# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    sum = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for rowno,row in enumerate(rows,start=2):
        record = dict(zip(headers,row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            sum += nshares * price
        # This catches errors in int() and float() conversions above
        except ValueError as e:
            print(f'Row {rowno}: Bad row: {row}')
    # print(f'Total cost {sum}')
    f.close()
    return sum
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost((filename))
print('Total cost:', cost)