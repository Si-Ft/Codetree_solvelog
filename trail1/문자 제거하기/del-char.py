a=input()+' '
while len(a) > 2:
    idx=int(input())
    if idx >= len(a)-1:
        a=a[:-2]+' '
    elif idx==0:
        a=a[1:]
    else:
        a=a[:idx]+a[idx+1:]
    print(a)
