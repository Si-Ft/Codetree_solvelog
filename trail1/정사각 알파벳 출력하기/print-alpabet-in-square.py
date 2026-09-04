N=int(input())
c = 64
for i in range(N):
    for j in range(N):
        c += 1
        print(chr(c), end='')
    print()