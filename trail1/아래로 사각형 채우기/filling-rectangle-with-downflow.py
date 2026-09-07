N=int(input())
ans=[[(i*N)+(j+1) for i in range(N)] for j in range(N)]
for i in range(N):
    print(*ans[i])