n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
y, x = 0, 0
dy = {'N':1, 'S':-1, 'E':0, 'W':0}
dx = {'N':0, 'S':0, 'E':1, 'W':-1}
for di, d in moves:
    y += dy[di] * int(d)
    x += dx[di] * int(d)
print(x, y)