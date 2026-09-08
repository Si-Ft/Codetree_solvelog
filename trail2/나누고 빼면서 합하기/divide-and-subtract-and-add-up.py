n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
# Please write your code here.
while m>1:
    ans += A[m-1]
    if m%2==1:
        m-=1
    else:
        m//=2
print(ans+A[0])