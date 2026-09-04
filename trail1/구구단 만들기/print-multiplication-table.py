A,B = map(int, input().split())
for j in range(1, 10):
    for i in range(B, A-1, -2): 
        print(f"{i} * {j} = {i * j}", end="")
        if i > A+1:
            print(" /", end=" ")
    print()
