N=int(input())
rep = 2 if N%5==0 else 10
a = [(i+1)*N for i in range(rep)]
print(*a)