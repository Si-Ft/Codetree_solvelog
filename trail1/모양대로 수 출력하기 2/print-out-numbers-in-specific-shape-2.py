N=int(input())
cnt=0
for i in range(N):
    for j in range(N):
        cnt+=2
        if cnt==10:
            cnt=2
        print(cnt, end=' ')
    print()