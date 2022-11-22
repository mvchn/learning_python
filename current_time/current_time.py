from datetime import datetime

now = datetime.now()
current_minute = int(now.strftime("%M"))
if current_minute % 2 != 0:
    print('YES! Current minute is odd')
else:
    print("NO! Current minute is even")

print(current_minute)
