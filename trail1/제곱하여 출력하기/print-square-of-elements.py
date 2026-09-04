N=int(input())
a=list(map(int,input().split()))
a2 = [n**2 for n in a]
print(*a2)