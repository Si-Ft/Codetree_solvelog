n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grid = [[0] * 201 for _ in range(201)] 
for i in range(n):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            grid[y][x] = i%2

ans = 0
for g in grid:
    for v in g:
        ans += v
print(ans)