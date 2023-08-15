n=int(input())
a=0
b=1
print(a,b,end=" ")
while(n-2>0):
    c=a+b
    a=b
    b=c
    n-=1
    print(c,end=" ")