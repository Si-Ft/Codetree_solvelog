a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
ans=0
for i in range(a,b+1):
    ans += i if is_prime(i) else 0
print(ans)