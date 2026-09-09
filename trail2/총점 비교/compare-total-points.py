n = int(input())

students = [
    (name, int(s1), int(s2), int(s3))
    for name, s1, s2, s3 in (input().split() for _ in range(n))
]
# Please write your code here.
students.sort(lambda x:sum(x[1:]))
for i in range(n):
    print(*students[i])