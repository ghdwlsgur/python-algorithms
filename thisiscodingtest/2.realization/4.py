
# 나의 풀이
# n, m = map(int, input().split())
# now_x, now_y, now_d = map(int, input().split())
#
# # 북쪽, 서쪽, 남쪽, 동쪽 (왼쪽 방향 순으로 배치)
# direction = [0, 3, 2, 1]
#
# my_map = []
# for _ in range(m):
#     my_map.append(list(map(int, input().split())))
#
# move_cnt = 1
# reset = 0
# while True:
#     now_d = direction[(int(direction.index(now_d) % 4) + 1) % 4]
#
#     if now_d == 0:  # 북쪽
#         next_x, next_y = now_x - 1, now_y
#         move_cnt += 1
#     elif now_d == 3:  # 서쪽
#         next_x, next_y = now_x, now_y - 1
#         move_cnt += 1
#     elif now_d == 2:  # 남쪽
#         next_x, next_y = now_x + 1, now_y
#         move_cnt += 1
#     elif now_d == 1:  # 동쪽
#         next_x, next_y = now_x, now_y + 1
#         move_cnt += 1
#
#     if 0 <= next_x < n and 0 <= next_y < m and my_map[next_x][next_y] == 0:
#         my_map[next_x][next_y] = 1
#         now_x, now_y = next_x, next_y
#         reset = 0
#     else:
#         reset += 1
#         if reset == 4:  # 모든 방향을 검사한 경우
#             break
#
#
# print(move_cnt)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


# 동빈나 풀이
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


