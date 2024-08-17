import datetime
from datetime import date
from datetime import timedelta
year=input()
month=input()
date=1
h=0
m=0
s=0
a=datetime.datetime(year,month,date,h,m,s)
b=datetime.datetime.now()
print("now time :",b)
s=a.strftime("%d/%m/Y,%H:%M:%S")
f=a.strftime("%d/%m/%Y")
u=b.strftime("%d/%m/%Y")
dif=b-a
print dif
print dif.weekday()
z=dif+timedelta(days=10)
print ("days",z)
print("day",dif.days)
print f
print (s)
