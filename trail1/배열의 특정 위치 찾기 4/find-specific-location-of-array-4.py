arr = list(map(int,input().split()))
c=0 
s=0
for i in range(10):
    if arr[i]==0:
        break
    c += 1 if arr[i]%2==0 else 0
    s += arr[i] if arr[i]%2==0 else 0
print(c,s)