n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str = [s for s in str if s[0:len(t)]==t]
str.sort()
print(str[k-1])