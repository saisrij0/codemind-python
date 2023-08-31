n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
for i in d:
    if d[i]>1:
        c=c+d[i]//2
print(c)