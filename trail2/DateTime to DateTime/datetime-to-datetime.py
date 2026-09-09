a, b, c = map(int, input().split())

# Please write your code here.
st = 1440*11+60*11+11
en = 1440*a+60*b+c
print(en-st if en>=st else -1)