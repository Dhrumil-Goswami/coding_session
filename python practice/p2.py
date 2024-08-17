from datetime import datetime
from datetime import timedelta
now = datetime.now() # current date and time
print now
last=datetime(2017,3,2,0,0,0)
print last
t=(now-last)
#c=timediffranceinminute=t/timedelta(minutes=1)
print t
print t.days

year = now.strftime("%Y")
print("year:", year)    
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)


#if you want to find future date 
# dt = current_datetime.date()
# print('Current Date:', dt)
# dt_tomorrow = dt + timedelta(days=1)
# print('Tomorrow Date:', dt_tomorrow)