binary = input()

# Please write your code here.
ans = 0
m = 1
for bit in binary[::-1]:
    ans += int(bit)*m
    m<<=1
print(ans)