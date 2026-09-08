text = input()
pattern = input()

# Please write your code here.
def find_idx():
    try:
        return text.index(pattern)
    except:
        return -1
print(find_idx())