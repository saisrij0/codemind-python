n=int(input())
s=n*n
c=0
t=n
while n>0:
   n=n//10;
   c+=1
if t==s%(10**c):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
