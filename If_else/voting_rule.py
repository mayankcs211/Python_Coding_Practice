# Write a program to check whether a person is eligible for voting or not. (accept age from user)

age = int(input('Enter your Age : '))

if age >= 1:
    if 1 < age < 18 :
        print('Under Age')
    else:
        print('Eligible to Vote')