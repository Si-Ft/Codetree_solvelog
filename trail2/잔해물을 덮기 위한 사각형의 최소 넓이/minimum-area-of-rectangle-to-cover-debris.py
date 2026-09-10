x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
adj_x, adj_y = False, False
# y, x축 기준으로 사각형 다 가리는 경우 
if y1[0]>=y1[1] and y2[0]<=y2[1]:
    adj_x = True
if x1[0]>=x1[1] and x2[0]<=x2[1]:
    adj_y = True

if adj_x and adj_y == True:
    print(0)
    exit()
if adj_x:
    if x1[0]<=x1[1] and x2[0]<=x2[1]:
        x2[0] = x1[1]
    elif x1[0]>=x1[1] and x2[0]>=x2[1]:
        x1[0] = x2[1]
if adj_y:
    if y1[0]<=y1[1] and y2[0]<=y2[1]:
        y2[0] = y1[1]
    elif y1[0]>=y1[1] and y2[0]>=y2[1]:
        y1[0] = y2[1]

print((x2[0]-x1[0]) * (y2[0]-y1[0]))