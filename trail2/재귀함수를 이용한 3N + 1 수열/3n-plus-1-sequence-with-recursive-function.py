n = int(input())

# Please write your code here.
def n_def(n):
    if n<=1:
        return 0
    n = n//2 if n%2==0 else n*3+1
    return n_def(n)+1
print(n_def(n))