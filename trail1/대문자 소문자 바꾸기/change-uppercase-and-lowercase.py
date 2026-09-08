a=input()
b=a.upper()
c=a.lower()
for idx, s in enumerate(a):
    if 'A'<=s<='Z':
        print(c[idx], end='')
    else:
        print(b[idx], end='')