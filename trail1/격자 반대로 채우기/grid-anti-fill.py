N=int(input())

# Please write your code here.
ans=[[0 for _ in range(N)] for _ in range(N)]
cnt=N*N
for x in range(N):
    if (N-x)%2!=0:
        for y in range(N):
            ans[y][x] = cnt
            cnt-=1
    else:
        for y in range(N-1,-1,-1):
            ans[y][x] = cnt
            cnt-=1
    
for i in range(N):
    print(*ans[i])