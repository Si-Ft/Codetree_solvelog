n = int(input())

# Please write your code here.
def pr_inc(cur, n):
    print(cur, end=' ')
    if cur==n:
        return
    pr_inc(cur+1, n)
def pr_dec(n):
    print(n, end=' ')
    if n==1:
        return
    pr_dec(n-1)
pr_inc(1, n)
print()
pr_dec(n)