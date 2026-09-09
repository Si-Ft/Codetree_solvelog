n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
chk = [0]*2001
pos = 1000
for i in range(n):
    st = pos
    en = pos
    dx = x[i] if dir[i]=='R' else -x[i]
    if dx>0:
        en = st+dx
    else:
        st = st+dx
    pos += dx
    
    chk[st:en] = [x+1 for x in chk[st:en]]

ans = 0
for i in chk:
    if i>=2:
        ans += 1
print(ans)