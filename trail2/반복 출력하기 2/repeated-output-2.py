n = int(input())

# Please write your code here.
def pr_hw(n):
    if n==0:
        return
    print('HelloWorld')
    pr_hw(n-1)
pr_hw(n)