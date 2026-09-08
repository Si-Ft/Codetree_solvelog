a, b = map(int, input().split())

# Please write your code here.
def is_on(n):
    if n%2==0:
        return False
    if n%10==5:
        return False
    if n%9 in [3,6]:
        return False
    return True

ans=0
for i in range(a,b+1):
    ans += 1 if is_on(i) else 0
print(ans)