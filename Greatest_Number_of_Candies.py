n=int(input())
l=list(map(int,input().split()))
g=int(input())
m=max(l)
for i in l:
    if i+g>=m:
        print(True,end=" ")
    else:
        print(False,end=" ")