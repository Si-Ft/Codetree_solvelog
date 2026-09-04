N=int(input())
cnt=0
for i in range(N):
    for j in range(N):
        cnt+=1
        if cnt==10:
            cnt=1
        print(cnt, end='')
    print()