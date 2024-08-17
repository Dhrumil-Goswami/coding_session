import datetime
from datetime import timedelta
s1 = "2010 Jan 1"
s2 = '31-1-2000' 
s3 = 'October10,1996, 10:40pm'

# Solution
from dateutil.parser import parse
print(parse(s1))
print(parse(s2))
print(parse(s3))