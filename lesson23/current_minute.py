from datetime import datetime

odd_minutes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 17, 29]

current_minute = datetime.today().minute

if current_minute in odd_minutes:
    print('YES! Current minute is odd')
else:
    print('NO! Current minute is even')

print(current_minute)
