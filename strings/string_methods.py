

s = '1 w 2 r 3g'
s = s.split(' ')

print(f'Input String : {s}')

string = []
for i in s:
    string.append(i.capitalize())

s = ' '.join(string)

print(f'Output String : {string}')