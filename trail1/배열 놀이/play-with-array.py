N,Q=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(Q):
    quer = list(map(int,input().split()))
    if quer[0] == 1:
        print(arr[quer[1]-1])
    elif quer[0] == 2:
        try:
            print(arr.index(quer[1]) + 1)
        except ValueError:
            print(0)
    else:
        print(*arr[quer[1]-1:quer[2]])