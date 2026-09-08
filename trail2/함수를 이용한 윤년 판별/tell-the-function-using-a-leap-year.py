y = int(input())

# Please write your code here.
def is_yoon(n):
    if n%100==0 and n%400!=0:
        return False
    if n%4==0:
        return True
    return False
print('true' if is_yoon(y) else 'false')