from datetime import datetime
from datetime import timedelta
a=datetime(2017,2,1,0,0,0)
b=datetime.now()
diff=b-a
print diff 
c=diff.strftime("%Y,%m,%d")
print c
# for i in range(c):
#     l=[]
#     if (diff.weekdays(i==1)):
#         l.append(i)
# print l.count()            