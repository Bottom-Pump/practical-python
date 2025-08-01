# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    sum = 0
    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        try:
            shares = int(row[1])
            price = float(row[2].strip())
            sum += shares * price
        except ValueError as e:
            print(f'Warning: Skip invalid lines [{line.strip()}]:{e}')
    # print(f'Total cost {sum}')
    f.close()
    return sum
cost = portfolio_cost(('Data/portfolio.csv'))
print('Total cost:', cost)