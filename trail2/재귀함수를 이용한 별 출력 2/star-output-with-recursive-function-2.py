n = int(input())

# Please write your code here.
def pr_star(cur,en):
    if cur!=0:
        print('* '*abs(cur))
    if cur==en:
        return
    pr_star(cur+1,en)
pr_star(-n, n)