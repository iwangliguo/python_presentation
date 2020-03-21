def sys(x,y):
    c=["A","B","C","D","E"]
    if x<y:
        print x,
    else:
        a=x/y
        b=x%y
        sys(a,y)
        if b<10:
            print b,
        else:
            print c[b-11],
