n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 101
for st, en in segments:
    blocks[st:en+1] = [x+1 for x in blocks[st:en+1]]
print(max(blocks))
# print(*blocks[:10])