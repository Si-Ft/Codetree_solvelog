N = int(input())

# Please write your code here.
def n_fib(n):
    if n in [1,2]:
        return 1
    return n_fib(n-1)+n_fib(n-2)
print(n_fib(N))