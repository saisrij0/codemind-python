n=int(input())
s=str(n)
for i in range(1,10):
    i=n%10
if len(s)!=10:
    print("Invalid")
if len(s)==10 and i!=0:
    print("Valid")