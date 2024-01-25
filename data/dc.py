import datetime
import time

today = datetime.datetime.now()
day = datetime.datetime(today.year,today.month,today.day)
print(time.ctime(day.timestamp()))
