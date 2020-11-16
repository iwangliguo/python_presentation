from math import *
def main():
    y=raw_input("please input a hanshu:")
    a=input("please input a qujian:")
    m=input("please input a fenshu:")
    z=S(y,a,m)
    print (z)
    return

def abc(y,a):
    x=a
    v=eval(y)
    return v
def S(y,a,m):
    s=0
    p=float(a[1]-a[0])
    for i in range(1,m+1):
        s+=p/6/m*(abc(y,a[0]+(2*i-2)*p/2/m)+4*abc(y,a[0]+(2*i-1)*p/2/m)\
                  +abc(y,a[0]+(2*i-2)*p/2/m))
    return s
