import statistics
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(0,n+1, 2):
    print(statistics.median(arr[:i+1]), end=' ')