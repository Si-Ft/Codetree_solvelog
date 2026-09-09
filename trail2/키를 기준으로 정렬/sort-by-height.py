n = int(input())
stat = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    stat.append((n_i,int(h_i),int(w_i)))

# Please write your code here.
stat.sort(lambda x:x[1])
for i in stat:
    print(*i)