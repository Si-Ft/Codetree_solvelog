N = int(input())

# Please write your code here.
def n_def(n):
    if n<=2:
        return n
    return n_def(n//3)+n_def(n-1)
print(n_def(N))