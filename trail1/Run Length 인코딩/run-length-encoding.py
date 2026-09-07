A = input()
A += ' '
# Please write your code here.
res=''
recent=A[0]
cnt=1
for c in A[1:]:
    if c==recent:
        cnt+=1
        continue
    res += recent+str(cnt)
    recent=c
    cnt=1
print(len(res))
print(res)