A,B = map(int, input().split())
for j in range(2, 10, 2):
    for i in range(B, A-1, -1): 
        print(f"{i} * {j} = {i * j}", end="")
        if i > A:
            print(" /", end=" ")
    print()
