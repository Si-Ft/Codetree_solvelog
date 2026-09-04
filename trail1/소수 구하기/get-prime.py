N=int(input())
cnt=0
for i in range(2, N+1):
    s = 0
    for j in range(2,i):
        s += 1 if i%j==0 else 0
    print(f"{i} " if s==0 else '', end='')
