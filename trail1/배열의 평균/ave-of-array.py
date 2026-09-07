arr = [list(map(int,input().split())) for _ in range(2)]
print(f"{sum(arr[0])/4:.1f} {sum(arr[1])/4:.1f}")
for i in range(4):
    print(f"{(arr[0][i]+arr[1][i])/2:.1f}", end=' ')
print(f"\n{(sum(arr[0])+sum(arr[1]))/8:.1f}")