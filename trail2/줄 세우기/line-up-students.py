n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
students.sort(lambda x:(-x[0], -x[1], x[2]))
for i in range(n):
    print(*students[i])