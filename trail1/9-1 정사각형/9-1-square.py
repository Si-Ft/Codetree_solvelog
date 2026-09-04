N=int(input())
cnt=10
for i in range(N):
    for j in range(N):
        cnt-=1
        if cnt==0:
            cnt=9
        print(cnt, end='')
    print()