N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    s = 0
    for i in range(a+1 if a%2==1 else a, b+1, 2):
        s += i
    print(s)