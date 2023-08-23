m=int(input())
n=int(input())
for i in range(m,n):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0 and i!=1:
        print(i)