a=input()
b=input()
cnt = 0
for i in range(len(a)-1):
    tar = a[i:i+2]
    cnt += 1 if tar == b else 0
print(cnt)