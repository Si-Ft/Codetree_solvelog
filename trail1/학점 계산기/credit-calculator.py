N=int(input())
h=list(map(float, input().split()))
s=sum(h)/N
print(f"{s:.1f}")
print("Perfect" if s>=4.0 else("Good" if s>=3.0 else "Poor"))