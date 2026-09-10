n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
field = [{'L':0, 'R':0, 'recent':'X'} for _ in range(200*n + 1)]
cur = 100*n
for i in range(n):
    num, d = x[i], dir[i]
    num -= 1
    if d == 'R':
        for j in range(num+1):
            field[cur+j]['R'] += 1   
            field[cur+j]['recent'] = 'R'
        cur += num
    else:
        for j in range(num+1):
            field[cur-j]['L'] += 1
            field[cur-j]['recent'] = 'L'
        cur -= num

Ls, Rs, Gs = 0, 0, 0
for i in range(200*n + 1):
    if field[i]['recent'] == 'X':
        continue
    if field[i]['L'] >= 2 and field[i]['R'] >= 2:
        Gs += 1
    elif field[i]['recent'] == 'L':
        Ls += 1
    elif field[i]['recent'] == 'R':
        Rs += 1

print(Ls, Rs, Gs)