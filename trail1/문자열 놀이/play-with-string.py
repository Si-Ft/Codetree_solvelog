s,Q = input().split()
s = list(s.strip())
for _ in range(int(Q)):
    n,a,b = input().split()
    if n=='1':
        a=int(a)    
        b=int(b)
        s[a-1], s[b-1] = s[b-1], s[a-1]
    else:
        s = [b if ch==a else ch for ch in s]
    print(''.join(s))