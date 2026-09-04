N=int(input())
for i in range(N):
    blank = i
    fill = (N*2-1)-2*i
    print("  "*blank, end='')
    print("* "*fill, end='')
    print("  "*blank, end='')
    print()