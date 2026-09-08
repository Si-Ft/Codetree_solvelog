Y, M, D = map(int, input().split())

# Please write your code here.
def get_month_table(y):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if y%4==0:
        days[2]=29
    if y%100==0:
        days[2]=28
    if y%400==0:
        days[2]=29
    return days

def is_valid(y,m,d):
    days = get_month_table(y)
    if m>12:
        return False
    if d>days[m]:
        return False
    return True

def get_season(m):
    if m==12:
        m=0
    if m<6:
        if m<3:
            return "Winter"
        else:
            return "Spring"
    else:
        if m<9:
            return "Summer"
        else:
            return "Fall"
    return -1

if not is_valid(Y,M,D):
    print(-1)
else:
    print(get_season(M))