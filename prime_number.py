n=int(input())
c=0
for i in range(2,n//2):
    if n%i==0:
        c+=1
if(c==0):
    print("prime")
else:
    print("not a prime")