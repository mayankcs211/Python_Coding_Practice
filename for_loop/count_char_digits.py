sample_data = 'Python 3.9'

digits = 0
chars = 0
for i in sample_data:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        chars += 1

print(digits)
print(chars)
