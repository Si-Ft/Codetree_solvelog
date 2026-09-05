arr=list(map(int,input().split()))
f = [0]*10
for i in range(len(arr)):
    if arr[i]==0:
        break
    f[arr[i]//10] += 1
for i in range(1,10):
    print(i,'-',f[i])
