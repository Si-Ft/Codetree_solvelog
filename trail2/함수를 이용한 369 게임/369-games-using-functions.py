a, b = map(int, input().split())

# Please write your code here.
def is_contain369(n):
    n = str(n)
    return n.count('3')+n.count('6')+n.count('9') != 0
def is_3b(n):
    return n%3==0

cnt=0
for i in range(a,b+1):
    cnt += 1 if is_contain369(i) or is_3b(i) else 0
print(cnt)