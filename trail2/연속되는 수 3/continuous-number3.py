N = int(input())
arr = [0] + [int(input()) for _ in range(N)] + [0]

# Please write your code here.
max_comb = 1
comb = 1
for i in range(1,len(arr)):
    if arr[i-1] * arr[i] <= 0:
        max_comb = max(comb, max_comb)
        comb = 1
    else:
        comb += 1
print(max_comb)