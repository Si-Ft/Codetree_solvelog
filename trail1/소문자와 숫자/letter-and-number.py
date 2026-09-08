a=input()
a="".join([s for s in a if 'a'<=s<='z' or 'A'<=s<='Z' or '0'<=s<='9'])
print(a.lower())