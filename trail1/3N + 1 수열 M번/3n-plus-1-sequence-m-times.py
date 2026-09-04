def quer(n):
    cnt = 0
    while n!=1:
        n = n//2 if n%2==0 else n*3+1
        cnt += 1
    return cnt

M=int(input())
for _ in range(M):
    N = int(input())
    print(quer(N))