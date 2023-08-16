n=int(input())
x=n
s=str(n)
su=0
l=len(s)
while n!=0:
    r=n%10
    su=su+(r**l)
    n=n//10
    l-=1
if su==x:
    print(True)
else:
    print(False)