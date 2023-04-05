# 현재 나이트의 위치
loc = input()
#print(loc)
# 나이트 위치 (x, y) 좌표 숫자로 표현
x = int(loc[1])
y_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = y_list.index(loc[0])+1
#print(x, y)
# 나이트가 움직일 수 있는 방향 8가지
way = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0

for i in way:
    nx = x + i[0]
    ny = y + i[1]
    #print(nx, ny)
    # 이동가능하면 count 증가
    if (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
        count += 1

print(count)