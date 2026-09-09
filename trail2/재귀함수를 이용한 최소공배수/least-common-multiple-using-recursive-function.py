import math
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def lcm(a, b):
    return (a * b) // math.gcd(a, b)
def n_def(c, cur):
    global arr
    if c==n:
        return cur
    return n_def(c+1, lcm(cur, arr[c]))
print(n_def(0, 1))