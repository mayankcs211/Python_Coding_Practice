input = input('Enter the string')

for i in input:
    if i.isalpha():
        print(f'{i} is alphabet.')
    else:
        print('Not a character')