N=int(input())
for i in range(N):
    blank = (N-1)-i
    fill = i*2+1
    print("  "*blank, end='')
    print("* "*fill, end='')
    print("  "*blank, end='')
    print()