a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calc(a,o,c):
    if o not in ['+','-','*','/']:
        print('False')
        return
    ans=None
    if o=='+':
        ans=a+c
    elif o=='-':
        ans=a-c
    elif o=='*':
        ans=a*c
    elif o=='/':
        ans=a//c

    print(a,o,c,'=',ans)
calc(a,o,c)