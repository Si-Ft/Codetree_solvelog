N=int(input())
ans=[[1 for _ in range(N)] for _ in range(N)]
print(*ans[0])
for i in range(1,N):
    for j in range(1,N):
        ans[i][j] = ans[i-1][j] + ans[i][j-1] + ans[i-1][j-1]
    print(*ans[i])