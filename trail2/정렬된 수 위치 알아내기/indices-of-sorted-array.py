n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
seq = []
for i, s in enumerate(sequence):
    seq.append((s,i))
seq.sort()
ans = [0] * n

for i, s in enumerate(seq):
    ans[s[1]] = i+1

print(*ans)