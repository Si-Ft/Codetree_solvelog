N=int(input())
cnt = 0
for i in range(0,N):
    for j in range(0,N):
        if i <= j:
            cnt+=1
        if cnt==10:
            cnt=1
        print(cnt if i <= j else ' ', end=' ')
    print()