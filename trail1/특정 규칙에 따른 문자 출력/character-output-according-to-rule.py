N=int(input())
for i in range(N*2-1):
    left = max(0, N-1-i)
    right = max(0, i-N+1)
    mid = N-left-right
    print('  '*left, end='')
    print('@ '*mid, end='')
    print('  '*right, end='')
    print()