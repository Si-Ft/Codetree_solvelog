N = int(input())

# Please write your code here.
arr = [i for i in range(1,N+1)]
print(*arr[::-1], *arr)