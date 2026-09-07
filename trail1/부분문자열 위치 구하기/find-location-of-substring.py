input_str = input()
target_str = input()

# Please write your code here.
idx = -1
try:
    idx = input_str.index(target_str)
except:
    pass
print(idx)