N=int(input())
for i in range(1,N+1):
    blank = (i-1)*2
    fill = N-i+1
    print("*"*fill, end='')
    print(" "*blank, end='')
    print("*"*fill, end='')
    print()