cnt=0
s=[]
while True:
    a=input()
    if a=='0':
        break
    cnt+=1
    if cnt%2!=0:
        s.append(a)
print(cnt, *s, sep='\n')