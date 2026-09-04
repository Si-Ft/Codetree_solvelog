arr = list(map(int,input().split()))
idx=10
for i in range(len(arr)):
    if arr[i] >= 250:
        idx=i
        break

s = sum(arr[:idx])
print(s, f"{s/idx:.1f}")