a, b = map(int, input().split())
n = input()
if n=='0':
    print(0)
    exit()

# Please write your code here.
def jinsu_to_hex(s, jin):
    ans = 0
    m = 1
    for n in s[::-1]:
        ans += int(n)*m
        m*=jin
    return ans

def hex_to_jinsu(n, jin):
    ans = []
    while n:
        ans.append(n%jin)
        n //= jin
    return ans[::-1]

n = jinsu_to_hex(n, a)
n = hex_to_jinsu(n, b)
print(*n, sep='')