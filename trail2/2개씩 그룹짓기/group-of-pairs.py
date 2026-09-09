n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
mx = 0
for i in range(n):
    mx = max(mx, nums[i]+nums[-i-1])
print(mx)