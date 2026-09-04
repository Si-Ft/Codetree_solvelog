N=int(input())
for i in range(1,N+1):
    r=N+1-i
    for j in range(N):
        if j%2==0:
            print(i,end='')
        else:
            print(r,end='')
    print()