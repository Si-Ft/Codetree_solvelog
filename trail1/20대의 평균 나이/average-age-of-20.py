s = 0
cnt = 0
while True:
    a=int(input())
    if not 20 <= a < 30:
        break
    s += a
    cnt += 1
print(f"{s / cnt:.2f}")