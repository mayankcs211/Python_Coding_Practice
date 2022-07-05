import os

# print(os.listdir())

for index, file in enumerate(os.listdir(), start=1):
    print(f'{index} : {file}')
