a=input()
ee = 0
eb = 0
for i in range(len(a)-1):
    tar = a[i:i+2]
    ee += 1 if tar == 'ee' else 0
    eb += 1 if tar == 'eb' else 0
print(ee,eb)