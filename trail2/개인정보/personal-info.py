n = 5

person = [
    (name, int(h), float(w))
    for name, h, w in (input().split() for _ in range(n))
]
# Please write your code here.
person.sort()
print("name")
for i in range(n):
    print(*person[i])
print()
print("height")
person.sort(lambda x:-x[1])
for i in range(n):
    print(*person[i])