arr=list(map(int,input().split()))
f = [0]*11
for i in range(len(arr)):
    if arr[i]==0:
        break
    f[arr[i]//10] += 1
for i in range(10,0,-1):
    print(i*10,'-',f[i])
