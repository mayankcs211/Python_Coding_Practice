start, end = input('Enter two numbers : ').split()

# print(start)
# print(end)

start = int(start)
end = int(end)

for i in range(start,end+1):
    if i%2 == 1:
        print(f'Prime no is : {i}')
    else:
        print('Not a prime')