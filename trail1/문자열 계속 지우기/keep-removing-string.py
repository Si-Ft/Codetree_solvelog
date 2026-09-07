A = input()
B = input()

# Please write your code here.
try:
    while True:
        A.index(B)
        A = A.replace(B,'')
except:
    pass
print(A)