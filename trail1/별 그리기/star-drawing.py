N=int(input())
for i in range(N*2-1):
    b = (N-1)-abs(N-1-i)
    blank = (N-1)-b
    fill = b*2+1
    print(" "*blank, end='')
    print("*"*fill, end='')
    print(" "*blank, end='')
    print()