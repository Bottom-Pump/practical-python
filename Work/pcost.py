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
    for row in rows:
        try:
            shares = int(row[1])
            price = float(row[2].strip())
            sum += shares * price
        except ValueError as e:
            print(f'Warning: Skip invalid lines {row}:{e}')
    # print(f'Total cost {sum}')
    f.close()
    return sum
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost((filename))
print('Total cost:', cost)