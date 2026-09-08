a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def is_2b(n):
    return sum(list(map(int,str(n).strip())))%2==0

ans=0
for i in range(a,b+1):
    ans += 1 if is_prime(i) and is_2b(i) else 0
print(ans)