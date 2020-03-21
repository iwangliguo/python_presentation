import string
def jz():
    x,y=input ("please input two numbers:")
    b=[]
    while x>=y:
          m=x
          x=x/y
          n=m%y
          print n,
          b.append(n)
          
    print x
    b=b+[x]
    print b
    revlist(b)

def revlist(list):
    if list!=[]:
        revlist(list[1:])
        print list[0],
    else:
        return


    
    
         
      
