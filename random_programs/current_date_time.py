from datetime import datetime

now = datetime.now()
print(f'Time Now : {now}')
print(f'Time Now : {now.strftime("%d-%b-%Y %H:%M:%S")}')