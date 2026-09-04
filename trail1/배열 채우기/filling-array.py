arr = list(map(int,input().split()))
st = 10
for i in range(10):
    if arr[i]==0:
        st = i-1
        break
print(*arr[st::-1])