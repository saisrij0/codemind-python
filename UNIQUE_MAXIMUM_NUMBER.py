n=int(input())
l=list(map(int,input().split()))
d={}
r=[]
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]==1:
        r.append(i)
if  r==[]:
    print(-1)
else:
    print(max(r))