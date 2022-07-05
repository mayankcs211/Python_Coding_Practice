total_units = int(input('Enter number of units : '))

if 1 <= total_units <= 100:
    print('No Charge')
elif 101 <= total_units <= 200:
    print(f'Total Charge : {0 + 5 * (total_units - 100)}')
elif total_units > 200:
    print(f'Total Charge : {500 + 10 * (total_units - 200)}')

