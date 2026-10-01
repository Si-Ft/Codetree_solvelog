from itertools import combinations

N, M = map(int,input().split())     # grid 크기, 남길 병원의 수
grid = [list(map(int,input().split())) for _ in range(N)]

person = []             # 사람들의 좌표
hospital = []           # 병원의 좌표
for y in range(N):
    for x in range(N):
        # 사람과 병원의 좌표를 grid로부터 하나하나 받아옴
        if grid[y][x] == 1:
            person.append((y,x))
        elif grid[y][x] == 2:
            hospital.append((y,x))

# 모든 사람 <-> 병원 간 모든 맨헤튼 거리를 미리 구함
# ptoh_dist[사람 idx][병원 idx]가 두 대상 사이 거리
ptoh_dist = [[0] * len(hospital) for _ in range(len(person))]
for pidx, paxis in enumerate(person):
    for hidx, haxis in enumerate(hospital):
        gy, gx = abs(paxis[0] - haxis[0]), abs(paxis[1] - haxis[1])
        ptoh_dist[pidx][hidx] = gy + gx

# 남길 병원의 index를 combinations를 통해 하나하나 불러와서 거리 합의 최소값을 찾아봄
gapmin = 2**30
for remain_hosp in combinations(range(len(hospital)), M):
    pminsum = 0     # 사람과 병원 거리 최소의 합
    for pidx in range(len(person)):
        pmin = 200
        for hidx in remain_hosp:
            pmin = min(pmin, ptoh_dist[pidx][hidx])
        pminsum += pmin
    gapmin = min(gapmin, pminsum)

print(gapmin)