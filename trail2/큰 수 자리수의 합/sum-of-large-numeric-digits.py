a, b, c = map(int, input().split())

# Please write your code here.
print( sum(list(map(int,str(a*b*c).strip()))))