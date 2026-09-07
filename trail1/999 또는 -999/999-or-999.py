arr=list(map(int,input().split()))
l = len(arr)
for i in range(l):
    if abs(arr[i])==999:
        l = i
        break
print(max(arr[:l]), min(arr[:l]))