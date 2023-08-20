n=int(input())
l=list(map(int,input().split()))
p=1
np=1
for i in l:
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        p*=i
    else:
        np*=i
if p>np:
    print(p-np)
else:
    print(np-p)