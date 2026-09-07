a=list(map(int,input().split()))
below=[num for num in a if num<500]
above=[num for num in a if num>=500]
print(max(below), min(above))