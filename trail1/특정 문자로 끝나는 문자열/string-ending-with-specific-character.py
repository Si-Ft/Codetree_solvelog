arr=[]
for _ in range(10):
    arr.append(input())
b=input()
cnt=0
for s in arr:
    if s[-1] == b:
        print(s)
        cnt=1
if cnt==0:
    print('None')