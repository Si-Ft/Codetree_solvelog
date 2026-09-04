N=int(input())
for i in range(N):
    for j in range(N):
        print(f"({i+1}, {j+1})", end=" ")
        if (i+j+2)%4==0:
            print()