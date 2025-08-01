# pcost.py
#
# Exercise 1.27
sum = 0
f = open("Data/portfolio.csv", 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    shares = int(row[1])
    price = float(row[2].strip())
    sum += shares * price
print(f'Total cost {sum}')
f.close()