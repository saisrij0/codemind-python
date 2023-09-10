n=int(input())
m=n
s=str(n)
l=len(s)
re=0
while n>0:
    r=n%10
    re=re+r**l
    n=n//10
    l-=1
if re==m:
    print(True)
else:
    print(False)