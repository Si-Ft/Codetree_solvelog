N=int(input())
for i in range(N):
    for j in range(N):
        flag='*'
        if i==0 or j==0 or i==N-1 or j==N-1:
            print(flag, end=' ')
            continue
        if i <= j:
            flag=' '
        print(flag, end=' ')
    print()