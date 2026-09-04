a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]==0:
        break
    print(a[i]+3 if a[i]%2==1 else a[i]//2, end=' ')