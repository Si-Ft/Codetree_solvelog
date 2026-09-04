N=int(input())
a=list(map(int,input().split()))
a2=[n for n in a if n%2==0]
print(*a2)