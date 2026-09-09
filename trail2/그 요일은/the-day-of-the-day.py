m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days=[0,31,29,31,30,31,30,31,31,30,31,30,31]
st = sum(days[:m1])+d1
en = sum(days[:m2])+d2
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
week_idx = week.index(A)
d = en-st
d = d//7 + (1 if week_idx<=(d%7) else 0)
print(d)
