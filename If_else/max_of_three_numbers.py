# take 3 inputs from User and find the max

num_1, num_2, num_3 = input('Enter the 3 numbers : ').split()
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

# if num_1 > (num_2 and num_3):
#     print(f'{num_1} is greater')
# elif num_2 > (num_3 and num_1):
#     print(f'{num_2} is greater')
# else:
#     print(f'{num_3} is greater')

if num_1 > num_2 and num_1 > num_3:
    print(f'{num_1} is greater')
elif num_2 > num_3 and num_2 > num_1:
    print(f'{num_2} is greater')
else:
    print(f'{num_3} is greater')