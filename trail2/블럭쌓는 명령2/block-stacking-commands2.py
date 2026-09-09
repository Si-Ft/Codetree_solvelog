n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0] * (n+1)
for st, en in commands:
    blocks[st:en+1] = [x+1 for x in blocks[st:en+1]]
print(max(blocks))