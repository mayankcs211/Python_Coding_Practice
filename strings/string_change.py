my_str = input('Enter the string ? ')

if len(my_str) >= 3:
    if my_str[-3:] != 'ing':
        new_str = my_str + 'ing'
    else:
        new_str = my_str + 'ly'

print(new_str)