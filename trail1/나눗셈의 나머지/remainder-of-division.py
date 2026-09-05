a,b=map(int, input().split())
f = [0] * 11
while a>1:
    f[a%b] += 1
    a//=b
print(sum([i**2 for i in f]))
