N = int(input())

# Please write your code here.
def n_sum(n):
    if n==1:
        return 1
    return n_sum(n-1)+n
print(n_sum(N))