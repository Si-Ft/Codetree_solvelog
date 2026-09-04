N=int(input())
cnt = 0
for _ in range(N):
    s = list(map(int,input().split()))
    if sum(s)//4 >= 60:
        cnt+=1
        print("pass")
    else:
        print("fail")
print(cnt)