N = input()

# Please write your code here.
def btoh(s):
    ans = 0
    m = 1
    for bit in s[::-1]:
        ans += int(bit)*m
        m<<=1
    return ans

def htob(n):
    ans = []
    while n:
        ans.append(n%2)
        n >>= 1
    return ans[::-1]

N = btoh(N)
N = htob(N*17)
print(*N, sep='')