# Write a program to check whether a number entered by user is even or odd.
num = int(input('Enter the number : '))

def odd_even(n):
    if num % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'

print(odd_even(num))

