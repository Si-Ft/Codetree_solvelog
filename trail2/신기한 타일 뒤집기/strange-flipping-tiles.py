n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
field = ['X' for _ in range(200*n + 1)]
cur = 100*n
for i in range(n):
    num, d = x[i], dir[i]
    num -= 1
    if d == 'R':
        for j in range(num+1):
            field[cur+j] = 'R'
        cur += num
    else:
        for j in range(num+1):
            field[cur-j] = 'L'
        cur -= num

Ls, Rs = 0, 0
for i in range(200*n + 1):
    if field[i] == 'X':
        continue
    elif field[i] == 'L':
        Ls += 1
    elif field[i] == 'R':
        Rs += 1

print(Ls, Rs)