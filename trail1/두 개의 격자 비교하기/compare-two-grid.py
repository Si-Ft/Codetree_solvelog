N,M=map(int,input().split())
a1=[list(map(int,input().split())) for _ in range(N)]
a2=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        print(0 if a1[i][j] == a2[i][j] else 1, end=' ')
    print()