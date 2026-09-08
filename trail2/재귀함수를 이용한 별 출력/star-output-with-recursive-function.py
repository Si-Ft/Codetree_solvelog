n = int(input())

# Please write your code here.
def pr_star(cur, N):
    print('*'*cur)
    if cur==N:
        return
    pr_star(cur+1, N)
pr_star(1, n)