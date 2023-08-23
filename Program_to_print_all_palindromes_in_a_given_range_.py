m=int(input())
n=int(input())
for i in range(m,n):
    c=i
    re=0
    while i>0:
        re=re*10+i%10
        i=i//10
    if re==c:
        print(c,end=" ")