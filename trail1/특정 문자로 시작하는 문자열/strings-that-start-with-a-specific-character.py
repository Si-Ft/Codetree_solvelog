arr=[]
N=int(input())
for _ in range(N):
    arr.append(input())
b=input()
cnt,sum=0,0
for s in arr:
    if s[0] == b:
        sum+=len(s)
        cnt+=1
print(f"{cnt} {sum/cnt:.2f}")