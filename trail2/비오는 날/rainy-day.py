n = int(input())
forecast = []

for i in range(n):
    d, dy, w = input().split()
    if w=='Rain':
        forecast.append((d, i, dy, w))

# Please write your code here.
forecast.sort()
print(forecast[0][0], *forecast[0][2:])