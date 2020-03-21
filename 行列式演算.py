
import copy

def hang(a):
    n=len(a[0])
    if n != 1:
        s=0
        for i in range(0,n):
            t=copy.deepcopy(a)
            t=t[1:]
            for j in range(n-1):
              del t[j][i]
            s+= (-1)**i*a[0][i]*hang(t)
        return s
    else:
        return a[0][0]






try:
    a=input("please enter a fangzhen:")
    if len(a)==len(a[0]):
        print hang(a)
    else:
        print "not fang"
except(SyntaxError):
    print"please replace your input"

