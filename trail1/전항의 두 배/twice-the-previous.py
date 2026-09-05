a,b=map(int,input().split())
print(a,b,end=' ')
for i in range(8):
    a,b=b,2*a+b
    print(b,end=' ')