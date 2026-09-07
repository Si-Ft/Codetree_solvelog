n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
freq = [0]*1001
for i in nums:
    freq[i] += 1
ans = -1
for i in range(1000,0,-1):
    if freq[i] == 1:
        ans = i
        break
print(ans)