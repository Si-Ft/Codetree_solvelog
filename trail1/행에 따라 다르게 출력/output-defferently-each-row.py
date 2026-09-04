N=int(input())
cnt=0
for i in range(N):
    for j in range(N):
        cnt += 1 if i%2==0 else 2
        print(cnt, end=' ')
    print()