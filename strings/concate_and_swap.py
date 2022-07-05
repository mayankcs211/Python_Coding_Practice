str_1, str_2 = input('Enter two strings :').split()

new_str_1 = str_2[:2] + str_1[2:]
new_str_2 = str_1[:2] + str_2[2:]

print(new_str_1)
print(new_str_2)

