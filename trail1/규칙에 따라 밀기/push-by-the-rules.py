a=input()
q=input()
for Q in q:
    if Q=='L':
        a=a[1:]+a[0]
    else:
        a=a[-1]+a[:-1]
print(a)