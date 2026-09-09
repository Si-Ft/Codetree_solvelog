N = int(input())

# Please write your code here.
def n_fact(n):
    if n<=1:
        return 1
    return n_fact(n-1)*n
print(n_fact(N))