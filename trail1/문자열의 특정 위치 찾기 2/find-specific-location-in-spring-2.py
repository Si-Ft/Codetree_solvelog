arr=["apple", "banana", "grape", "blueberry", "orange"]
a=input()
cnt=0
for s in arr:
    if a in s[2:4]:
        print(s)
        cnt+=1
print(cnt)