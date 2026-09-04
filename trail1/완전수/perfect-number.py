start, end = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(start, end+1):
    s = 0
    for j in range(1,i):
        s += j if i%j==0 else 0
    cnt += 1 if s==i else 0
print(cnt)