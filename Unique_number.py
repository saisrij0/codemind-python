n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
s=set(l)
if len(l)==len(s):
    print("Unique Number");
else:
    print("Not Unique Number");