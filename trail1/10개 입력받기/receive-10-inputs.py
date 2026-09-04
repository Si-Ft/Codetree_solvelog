arr = list(map(int,input().split()))
st = 10
for i in range(10):
    if arr[i]==0:
        st = i
        break
print(sum(arr[:st]), f"{sum(arr[:st])/st:.1f}"  )