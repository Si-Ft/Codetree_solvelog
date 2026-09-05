a=1
b=int(input())
print(a,b,end=' ')
while b<100:
    a,b=b,a+b
    print(b, end=' ')