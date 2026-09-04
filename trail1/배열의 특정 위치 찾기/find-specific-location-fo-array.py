a=list(map(int,input().split()))
a1 = sum(a[1::2])
a2 = sum(a[2::3]) / 3
print(f"{a1} {a2:.1f}")