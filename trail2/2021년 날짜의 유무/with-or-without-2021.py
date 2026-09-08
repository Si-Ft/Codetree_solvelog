M, D = map(int, input().split())

# Please write your code here.
def is_valid_date(m,d):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m>12:
        return False
    if d>days[m]:
        return False
    return True

print('Yes' if is_valid_date(M,D) else 'No')
    