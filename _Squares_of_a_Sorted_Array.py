n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(i*i)
x=sorted(s)
for j in x:
    print(j,end=" ")