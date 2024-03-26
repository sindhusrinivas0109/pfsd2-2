"""import datetime
import time
print(time.time())

datetime_sindhu = datetime.datetime.now()
print(datetime_sindhu)
print("Year: ",datetime_sindhu.year)

#calender
import calendar
s = calendar.prcal(3023)
s2 = calendar.month(2023,5)
s1 = calendar.isleap(2005)

print(s2)
print(s1)


x = datetime.datetime.now()
from datetime import timedelta
print(x + timedelta(days=-89))"""

#pytz - can print any country or any location time
import pytz
from datetime import datetime
time1 = pytz.timezone('Asia/seoul')
print("current Time is: ",datetime.now(time1))