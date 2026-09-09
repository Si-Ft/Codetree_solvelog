n = int(input())
if n==0:
    print(0)
# Please write your code here.
ans = []
while n:
    ans.append(n%2)
    n >>= 1
print(*ans[::-1], sep='')