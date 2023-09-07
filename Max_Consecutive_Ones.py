n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,n):
    c=0
    for j in range(i,n):
        if l[j]==1:
            c+=1
        else:
            break
    r.append(c)
print(max(r))