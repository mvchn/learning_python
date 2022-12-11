from datetime import datetime

now = datetime.now()
current_minute = int(now.strftime("%M"))
odd_minutes = list(range(1, 60, 2))
if current_minute in odd_minutes:
    print('YES! Current minute is odd')
else:
    print("NO! Current minute is even")

print(current_minute)

