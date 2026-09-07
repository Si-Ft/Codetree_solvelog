N1,N2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
res = 'No'
for i in range(N1-N2+1):
    if A[i:i+N2] == B:
        res = 'Yes'
print(res)