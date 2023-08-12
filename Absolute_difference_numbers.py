m,n=map(int,input().split());
l=m%(10**n);
while m>(10**n):
    m=m//10;
f=m;
if f>l:
    print(f-l);
else:
    print(l-f);