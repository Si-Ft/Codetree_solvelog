n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
p1 = [0]
p2 = [0]
for i in range(n):
    dx = 1 if d[i]=='R' else -1
    for _ in range(t[i]):
        p1.append(p1[-1] + dx)
for i in range(m):
    dx = 1 if d2[i]=='R' else -1
    for _ in range(t2[i]):
        p2.append(p2[-1] + dx)

ans = -1
for i in range(1, len(p1)):
    if p1[i]==p2[i]:
        ans = i
        break
print(ans)