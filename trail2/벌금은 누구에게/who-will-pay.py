N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
cnt = [0] * (N+1)
ans = -1
for i in student:
    cnt[i] += 1
    if cnt[i]>=K:
        ans = i
        break
print(ans)