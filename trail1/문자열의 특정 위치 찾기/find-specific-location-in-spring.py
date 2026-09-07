res = 'No'
a,b = input().split()
try:
    res = a.index(b)
except:
    pass
print(res)