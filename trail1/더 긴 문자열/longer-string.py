a,b=input().split()
ret='same'
if len(a)<len(b):
    ret=b
elif len(a)>len(b):
    ret=a
gap = max(len(a),len(b))
print(ret, gap if ret!='same' else '')
