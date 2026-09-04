N = int(input())
for i in range(N*2+1):
    for j in range(N*2+1):
        flag='*'
        if i%2==1 and j%2==1:
            flag=' '
        print(flag, end=' ')
    print()