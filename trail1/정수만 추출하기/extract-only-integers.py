a,b=input().split()
for i in range(len(a)):
    if not '0'<=a[i]<='9':
        a=a[:i]
        break
a=int(a)
for i in range(len(b)):
    if not '0'<=b[i]<='9':
        b=b[:i]
        break
b=int(b)
print(a+b)