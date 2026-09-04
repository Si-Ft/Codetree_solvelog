N=int(input())
for i in range(N):
    print("".join(map(str, [i+1 for _ in range(N)])))