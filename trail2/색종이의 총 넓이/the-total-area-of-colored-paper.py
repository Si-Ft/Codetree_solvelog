n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid = [[0] * 201 for _ in range(201)] 
for sx, sy in points:
    sy += 100
    sx += 100
    for y in range(sy, sy+8):
        for x in range(sx, sx+8):
            grid[y][x] = 1

ans = 0
for g in grid:
    for v in g:
        ans += v
print(ans)