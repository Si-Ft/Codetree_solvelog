m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
st = sum(days[:m1])+d1
en = sum(days[:m2])+d2
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(week[(en-st)%7])