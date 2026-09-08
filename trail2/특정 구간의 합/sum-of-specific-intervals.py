n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum_query(st,en):
    return sum(arr[st-1:en])

for st,en in queries:
    print(sum_query(st,en))