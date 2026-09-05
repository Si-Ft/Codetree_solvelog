f = [0] * 4
for i in range(3):
    a,b = input().split()
    c = 2 if int(b)<37 else 0
    c += 1 if a=='N' else 0
    f[c] += 1
if f[0]>=2:
    f.append('E')
print(*f)