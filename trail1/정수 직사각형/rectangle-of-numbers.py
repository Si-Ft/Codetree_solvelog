N,M=map(int,input().split())
arr=[[(j*M)+(i+1) for i in range(M)] for j in range(N)]
for i in range(N):
    print(*arr[i])