n=int(input())
c=0
for i in range(1,(n//2)+1):
    if n%i==0:
        c=c+i
if c==n:
    print("True")
else:
    print("False")