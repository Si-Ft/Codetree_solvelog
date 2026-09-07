ans=[[1 for _ in range(5)] for _ in range(5)]
print(*ans[0])
for i in range(1,5):
    for j in range(1,5):
        ans[i][j] = ans[i-1][j] + ans[i][j-1]
    print(*ans[i])