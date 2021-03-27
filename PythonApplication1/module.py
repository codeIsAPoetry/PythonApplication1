import math


def sum(x,y):
    return x+y

def div(x,y):
    return x/y

def mult(x,y):
    return x*y

def sub(x,y):
    return x-y

def recfact(x):
    if x==1:
        return x
    return x*recfact(x-1)

def recsum(lst):
    if lst==[]:
        return 0
    return lst[0]+recsum(lst[1:])


def recmult(lst):
    if lst==[]:
        return 1
    return lst[0]*recmult(lst[1:])

def recmax(x):
    if len(x)==2:
        return x[0] if x[0]>x[1] else x[1]
    opora = recmax(x[1:])
    return x[0] if x[0]> opora else opora

def mainFunction(A):
    s=int(A//1000)
    h=int((A-s*1000)//100)
    t = int((A-(s*1000)-h*100)//10)
    b = int(A-(s*1000)-(h*100)-t*10)
    return True if s==b and h==t else False



     

