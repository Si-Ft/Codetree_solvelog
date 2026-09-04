a=list(map(int,input().split()))
for i in range(100):
    if a[i]==0:
        print(sum(a[i-3:i]))
        break