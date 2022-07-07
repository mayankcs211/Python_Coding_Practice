my_str = input('Enter the string').split()

# print(type(my_str))
print(my_str)

word_length = 0

for i in my_str:
    if len(my_str[i]):
        print(f'Longest word is : {i} and length is {len(i)}')

