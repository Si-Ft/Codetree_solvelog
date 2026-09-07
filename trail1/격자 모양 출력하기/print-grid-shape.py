N,M=map(int,input().split())
arr=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    y,x=map(int,input().split())
    arr[y-1][x-1]=y*x
for i in range(N):
    print(*arr[i])