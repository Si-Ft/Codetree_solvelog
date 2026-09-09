N = int(input())

# Please write your code here.
def n_def(n):
    if n<=2:
        a=[2,4]
        return a[n-1]
    return n_def(n-1)*n_def(n-2)%100
print(n_def(N))