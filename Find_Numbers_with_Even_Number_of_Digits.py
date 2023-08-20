n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    d=0
    while i!=0:
        d+=1
        i=i//10
    if d%2==0:
        c+=1
print(c)