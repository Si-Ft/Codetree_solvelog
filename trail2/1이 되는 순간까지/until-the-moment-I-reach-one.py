N = int(input())

# Please write your code here.
def n_div(n):
    if n==1:
        return 0
    n = n//2 if n%2==0 else n//3
    return n_div(n)+1
print(n_div(N))