arr=[list(map(int,input().split())) for _ in range(4)]
ans = 0
for i in range(4):
    for j in range(4):
        if i>=j:
            ans+=arr[i][j]
print(ans)