n, m = map(int, input().split())

# Please write your code here.
ans=[[0 for _ in range(m)] for _ in range(n)]
cnt=0
for x in range(m):
    if x%2==0:
        for y in range(n):
            ans[y][x] = cnt
            cnt+=1
    else:
        for y in range(n-1,-1,-1):
            ans[y][x] = cnt
            cnt+=1
    
for i in range(n):
    print(*ans[i])