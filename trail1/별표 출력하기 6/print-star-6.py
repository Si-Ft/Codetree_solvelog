N=int(input())
for i in range(N*2-1):
    b=(N-1)-abs((N-1)-i)
    fill = (N*2-1)-b*2
    print("  "*b, end='')
    print("* "*fill, end='')
    print("  "*b, end='')
    print()