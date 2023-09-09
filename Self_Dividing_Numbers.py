m=int(input())
n=int(input())
for i in range(m,n+1):
    c=0
    res=0
    t=i
    while i>0:
        r=i%10
        if r>0:
            if t%r==0:
                res+=1
        i=i//10
        c+=1
    if res==c:
        print(t,end=" ")