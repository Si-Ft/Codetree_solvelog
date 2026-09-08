n = int(input())

# Please write your code here.
def is_even(n):
    return n%2==0
def is_5b(n):
    return sum(list(map(int,str(n).strip())))%5==0
if is_even(n) and is_5b(n):
    print('Yes')
else:
    print('No')