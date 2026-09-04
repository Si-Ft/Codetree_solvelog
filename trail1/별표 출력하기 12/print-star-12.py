N=int(input())
for i in range(N):
    for j in range(N):
        flag='*'
        if i > j:
            flag=' '
        if i != 0 and j%2 == 0:
            flag=' '
        print(flag, end=' ')
    print()