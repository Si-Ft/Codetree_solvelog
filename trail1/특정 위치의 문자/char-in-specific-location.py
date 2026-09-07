list = ['L','E','B','R','O','S']
a = input()
for i, val in enumerate(list):
    if val == a:
        print(i)
        break
    if i==5:
        print("None")