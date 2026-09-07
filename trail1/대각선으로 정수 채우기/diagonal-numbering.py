n, m = map(int, input().split())

# Please write your code here.
ans=[[0 for _ in range(m)] for _ in range(n)]
cnt=1
for b in range(n+m-1):
    for y in range(n):
        x = b-y
        if x<0 or x>=m:
            continue
        ans[y][x] = cnt
        cnt+=1
for i in range(n):
    print(*ans[i])