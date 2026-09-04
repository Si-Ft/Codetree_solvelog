N=int(input())
cnt=0
d=1
for i in range(N):
    for j in range(N):
        cnt+=d
        if cnt==N+1:
            cnt=N
            d=-1
        elif cnt==0:
            cnt=1
            d=1
        print(cnt, end='')
    print()