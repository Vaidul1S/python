# Date and Time

import datetime

date = datetime.date(2025, 6, 7)
today = datetime.date.today()
time = datetime.time(11, 55, 30)
now = datetime.datetime.now()
now = now.strftime("%m-%d-%Y %H:%M:%S")

target_datetime = datetime.datetime(2030, 2, 25, 8, 45, 0)
current_datetime = datetime.datetime.now()

print(date)
print(today)
print(time)
print(now)

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target day yet to pass!")