n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
mx = 0
for l in range(len(price)-1):
    for r in range(l+1, len(price)):
        mx = max(mx, price[r]-price[l])
print(mx)
