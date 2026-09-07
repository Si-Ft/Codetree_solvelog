n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
n+=1
while n!=1:
    n = a.index(max(a[:n-1])) + 1
    print(n, end=' ')
