n=int(input())
s=n*n
su=0
while s>0:
    su=su+s%10
    s=s//10
if su==n:
    print("Neon Number")
else:
    print("Not Neon Number")