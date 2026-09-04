N=int(input())
c = 64
for i in range(N):
    for j in range(i+1):
        c += 1
        if c > 90:
            c = 65
        print(chr(c), end='')
    print()