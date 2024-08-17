
# a="heloo"
# print a[::-1]

def bac(n):
    a=1
    if n==0:
        return 1
    else:
        return n*bac(n-1)
n=input("enter")
print bac(n)