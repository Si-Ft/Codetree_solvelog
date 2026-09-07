a=input()
n=int(input())
if len(a)<n:
    n=len(a)
print(a[:-n-1:-1])