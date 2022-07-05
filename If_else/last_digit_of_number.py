
n = int(input('Enter number : '))

print(f'Last digit of number is : {n%10}')


if (n%10) % 3 == 0:
    print('Divisible by 3')
else:
    print('Sorry')