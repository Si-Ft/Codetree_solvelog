a=list(map(int,input().split()))
od = sum(a[::2])
evn = sum(a[1::2])
print(abs(od-evn))