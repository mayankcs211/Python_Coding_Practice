str = input('Enter the string : ').split()

print(type(str))

str_list = list(str)
# print('str_list',str_list)

list1 =[]
list1[:0]=str[0]
list2 = []
list2[1:] = str[1]

print(list1)
print(list2)

str_even =''
str_odd = ''
for i in range(len(str)+1):
    if i % 2 == 1:
        str_odd += ''.join(list1[i])
        # print(str_even)
    else:
        str_even += ''.join(list2[i])