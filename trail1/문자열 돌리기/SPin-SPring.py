a=input()
L=len(a)
print(a)
for _ in range(L):
    a=a[-1]+a[:-1]
    print(a)