a=input()
a="".join([s for s in a if 'a'<=s<='z' or 'A'<=s<='Z'])
print(a.upper())