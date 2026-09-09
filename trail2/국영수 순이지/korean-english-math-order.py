n = int(input())

info = []

for _ in range(n):
    student_info = input().split()
    info.append(student_info)
# Please write your code here.
info.sort(lambda x:(-int(x[1]), -int(x[2]), -int(x[3])))
for i in range(n):
    print(*info[i])