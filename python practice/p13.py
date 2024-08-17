# def test(a,b):
#     c=a+b
#     print(c)
# a=input("1")
# b=input("2")
# test(a,b)


# def test1(a):
#     b=(a*60)
#     print(b)
#     return b
# a=input("min:")
# test1(a)
# dict1={'one':1,'two':2,'three':3}
# l=dict1.keys()
# m=dict1.values()
# print(l)
# print(m)
# dict2=dict(zip(m,l))
# print(dict2)
# str1="hello @wo#r&ld hello"
# str5=str1.split(" ")
# dict3={j:str5.count(j) for j in str5}
# print(dict3)

# dict1={i:str1.count(i) for i in str1}
# print (dict1)
# chr1=0
# print (str1.count(str1))
# print (len(str1))
# print(str1.strip())
# str3=str1.replace(" ","")
# print(str3)
# for i in range(len(str1)):
#     if (str1[i].isalpha()):
#         continue
#     elif(str1[i].isdigit()):
#         continue
#     else:
#         print(str1[i])
#         chr1=chr1+1
# print(chr1)

# l=[1,2,3]
# l.insert(0,4)
# print(l)
# t1=(1,2,3)
# print(id(t1))
# t1[3]=4
# dict1={'one':1,'two':2,'three':3}
# print(dict1)
# dict1[4]='four'
# print (dict1)
# net_amount = 0

# while True:
#     str = raw_input ("Enter transaction: ")
#     transaction = str.split(" ")
#     type = transaction [0]
#     amount = int (transaction [1])

#     if type=="D" or type=="d":
#         net_amount += amount
#     elif type=="W" or type=="w":
#         net_amount -= amount
#     else:
#         pass
#     str = raw_input ("want to continue (Y for yes) : ")
#     if not (str[0] =="Y" or str[0] =="y") :
#         break
# print "Net amount: ", net_amount
# Number = int(input(" Please Enter any Number: "))

# for i in range(2, Number + 1):
#     if(Number % i == 0):
#         print("iiiiiii",i)
#         isprime = 1
#         print("333333333", 8//3)
#         print("222222222", 8//2+1)
#         for j in range(2, (i // 2 + 1)):
#             print("jjjjjjjjjjjj", j)
#             if(i % j == 0):
#                 isprime = 0
#                 break

#         if (isprime == 1):
#             print(" %d is a Prime Factor of a Given Number %d" % (i, Number))

# n=input("enter Number")
# l=[]
# for i in range (2,n+1):
#     if (n%i==0):
#         print("dddddddddddddd",i)
#         l.append(i)
#         print(l)
#         for l in l:
#             if ()

# primt=1
# for j in range(2,(i//2+1)):
#     if (i%j==0):
#         primt=0
#         break
# if (primt == 1):
#         #     print("iiiiiiiiiii",i)
# import math

# def primeFactors(n):

#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         print 2,
#         n = n / 2

#     # n must be odd at this point
#     # so a skip of 2 ( i = i + 2) can be used
#     for i in range(2,int(math.sqrt(n))+1,2):

#         # while i divides n , print i ad divide n
#         while n % i== 0:
#             print i,
#             n = n / i

#     # Condition if n is a prime
#     # number greater than 2
#     if n > 2:
#         print n
# n = 40
# primeFactors(n)


# def factors(nr):
#     i = 2
#     factors = []
#     while i <= nr:
#         if (nr % i) == 0:
#             factors.append(i)
#             nr = nr / i
#         else:
#             i = i + 1
#     return factors


# nr = 30
# print (factors(nr))
# print(factors)


# def number(n)
#     c=2
#     d=[]
#     while (c<=n):
#         if (n%c)==0:
#             d.append(c)
#             n=n/c
#         else:
#             c=c+1
#     return number
#     n=20
# from datetime import date

# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year
#     return age
# print(calculateAge(date(1997, 2, 3)), "years")
# l1 = ['a', 'b', 'c', 'd','f','j']
# l2 = [1, 2, 3, 4,5,6,7,8]
# print(enumerate(l1))
# for i, v in enumerate(l2):
#     print("ii",i)
#     print("vv",v)
#     print (l1.insert(2 * i + 1, v))

# print(l1)

# from datetime import datetime, timedelta
# year = int(input('Enter a year'))
# month = int(input('Enter a month'))
# day = int(input('Enter a day'))
# date1 = datetime.date(year, month, day)
# print(date1)

# d = datetime.today() - timedelta(days=2)
# print( d)

# import datetime
# from datetime import timedelta
# date =datetime.datetime(int(input("year")),int(input('month')),int(input("date")),0,0,0)
# print(date.day-2)
# re=datetime.timedelta(5)
# print(re)
# heeerr=date-re
# print(heeerr)
# d=datetime.date(int(input("years")),int(input("month")),int(input("date")))
# gap=datetime.timedelta(10)
# print(d-gap)
# print(d)
# nm=int(input("enter the number "))
# a=0
# b=1
# for i in range (nm):
#     if (nm<=0):
#         print("enter valid number")
#     else:
#         c=a+b
#         a=b
#         b=c
#     print(c)
# a=0
# b=1
# def fib(n):
#     if (n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return (fib(n-1)-fib(n-2))
# print(fib(10))
# dict1 ={"a":1,"b":2,"c":3}
# dict1['a'].remove()
# How to get Odd and Even values from List L = [1,2, 3, 4,5,6,7,8,9,10]  ? Create Odd List and Even List from L.

# Output must be Odd = [1,3,5,7,9] Even = [2,4,6,8,10]
# L = [1,2, 3, 4,5,6,7,8,9,10]
# odd=[]
# Even=[]
# for i in L:
#     if(i%2==0):
#         odd.append(i)
#     else:
#         Even.append(i)
# print(odd,Even)
# T= (124, 136, 156)
# T=T+(250,)
# print("Tuple is :"T)
# list1 = [('c', 2), ('b', 6),('d', 7), ('a', 8),('e',6)]
# Output : [('a', 8),  ('b', 6), ('c', 2), ('d', 7), ('e',6)]
# print(sorted(list1))

# string_a = 'Hello Odoo World!'
# count_o=[]
# newlist=list(string_a)
# print(newlist)
# last_element=len(newlist)
# print(last_element)
# print(newlist.count('o'))
# first_element=newlist[0]
# print(newlist.count(first_element))
# for i in string_a:
#     if (i=='o'):
#         count_o.append(i)
# # print(count(count_o))
# D = {'A':1, 'B':2, 'C':3, 'c':4}
# {i:D[0] for i in D }
# D = {'A':1, 'B':2, 'C':3, 'c':4}
# del D[next(iter(D))]
# print("first key delete using index :",D)
string_a = 'Hello Odoo World!'
print(string_a)
print("first occurrence of letter in above string 'o:",string_a.find('o'))
print("last occurrence of letter in above string 'o:",string_a.rfind('o'))
#print("",newstring.find('o'))
# for i in string_a:
#     if (i=="O") and (i=='o'):
#         print(i.find())
