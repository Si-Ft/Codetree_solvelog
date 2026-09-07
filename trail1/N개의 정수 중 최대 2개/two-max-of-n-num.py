n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort(reverse=True)
print(*a[:2])