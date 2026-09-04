N=int(input())
res = 'N'
for i in range(2, N):
    if N%i==0:
        res = 'C'
print(res)