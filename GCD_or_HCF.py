a,b=map(int,input().split())
for i in range(a*b,0,-1):
    if a%i==0 and b%i==0:
        break
print(i)