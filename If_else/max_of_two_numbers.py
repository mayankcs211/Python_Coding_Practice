number_1 = int(input('Enter the 1st number of your choice ? '))
number_2 = int(input('Enter the 2nd number of your choice ? '))

if isinstance(number_1, int) and isinstance(number_2, int):
    if number_1 > number_2:
        print(f'{number_1} is greater')
    else:
        print(f'{number_2} is greater')
