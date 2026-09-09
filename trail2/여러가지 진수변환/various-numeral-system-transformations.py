N, B = map(int, input().split())

# Please write your code here.
ans = []
while N:
    ans.append(N%B)
    N //= B
print(*ans[::-1], sep='')