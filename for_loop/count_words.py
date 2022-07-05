string = input('Enter the string : ').split()

# print(len(string))
# print(string.count('is'))

my_new_str = []
count = 0
for i in string:
    if i not in my_new_str:
        my_new_str.append(i)
    elif i in my_new_str:
        count += 1
        continue

print(' '.join(my_new_str))
print(count)