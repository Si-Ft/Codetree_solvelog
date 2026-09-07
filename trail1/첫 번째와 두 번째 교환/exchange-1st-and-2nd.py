a=input()
s1=a[0]
s2=a[1]
tmp='0'
a = a.replace(s1,tmp)
a = a.replace(s2,s1)
a = a.replace(tmp,s2)
print(a)