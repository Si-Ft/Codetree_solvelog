N=int(input())
arr=[0]*N
arr[0] = 1
for i in range(N):
    tmp=arr[:]
    for j in range(1,i+1):
        tmp[j]=arr[j-1]+arr[j]
    arr=tmp[:]
    print(*arr[:i+1])