# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
months = 0

while principal > 0:
    months = months + 1
    if(principal < payment):
        print(f'{months}\t{total_paid+principal}\t0')
        break
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment

    if(months <= extra_payment_end_month and months >= extra_payment_start_month):
        principal -= 1000
        total_paid += 1000
        
    print(f'{months}\t{total_paid}\t{principal}')

print(f'Total paid:\t{total_paid}')
print(f'months:\t\t{months}')