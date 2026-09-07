N=int(input())
l,a=0,0
for _ in range(N):
    s=input()
    l += len(s)
    a += 1 if s[0]=='a' else 0
print(l,a)