n = int(input())

person = [
    (name, int(h), int(w))
    for name, h, w in (input().split() for _ in range(n))
]

# Please write your code here.
person.sort(lambda x:(x[1], -x[2]))
for i in range(n):
    print(*person[i])