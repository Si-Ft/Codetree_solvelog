n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 201
for st, en in segments:
    blocks[st+100:en+100] = [x+1 for x in blocks[st+100:en+100]]
print(max(blocks))
# print(*blocks[100:110])