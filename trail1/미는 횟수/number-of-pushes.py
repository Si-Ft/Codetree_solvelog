a=input()
b=input()
ans=-1
for i in range(len(b)):
    if a==b:
        ans = i
        break
    a=a[-1]+a[:-1]
print(ans)