a=list(map(int,input().split()))
for _ in range(8):
    a.append((a[-1]+a[-2])%10)
print(*a)