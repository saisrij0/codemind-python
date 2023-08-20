n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(0,n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e>o:
    if (e-o)%4==0:
        print('X')
    else:
        print('Y')
if o>e:
    if (o-e)%4==0:
        print('X')
    else:
        print('Y')