N=int(input())
cnt = 0
grid = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        cnt += 1
        grid[i][j] = cnt

for i in range(1,N,2):
    for j in range(N//2):
        grid[i][j], grid[i][N-1-j] = grid[i][N-1-j], grid[i][j]

for i in range(N):
    for j in range(N):
        print(grid[i][j], end=' ')
    print()