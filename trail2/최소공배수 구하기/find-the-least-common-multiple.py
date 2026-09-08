n, m = map(int, input().split())

# Please write your code here.
def lcm(n,m):
    for i in range(min(n,m), 10001, min(n,m)):
        if i%n==0 and i%m==0:
            return i
print(lcm(n,m))