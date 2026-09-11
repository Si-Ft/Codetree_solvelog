n, t = map(int, input().split())
arr = [1001] + list(map(int, input().split())) + [0]

if max(arr[1:]) <= t:
    print(0)
    exit()

# Please write your code here.
max_comb = 0
comb = 0
for i in range(1,len(arr)):
    if arr[i] <= t:
        max_comb = max(comb, max_comb)
        comb = 0
    else:
        comb += 1
print(max_comb)