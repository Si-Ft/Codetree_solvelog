n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
mx = 999
for l in range(len(price)-1):
    for r in range(l+1, len(price)):
        mx = min(mx, price[r]-price[l])
print(mx)
