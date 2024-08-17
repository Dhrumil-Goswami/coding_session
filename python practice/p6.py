from datetime import date

d1 = date(2019, 10, 6)
d2 = date(2019, 10, 20)
result = (d1-d2).days//7
print result