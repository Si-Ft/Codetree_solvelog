N = int(input())

# Please write your code here.
def n_sum2(n):
    if n==0:
        return 0
    return n_sum2(n//10)+(n%10)**2
print(n_sum2(N))