# 나의 풀이
#
# n = int(input()) # 공간의 크기 입력
# command = list((input().split())) # L, R, U, D 명령 입력
#
# # 배열 생성
# l = [[0 for _ in range(n)] for _ in range(n)]
# # 현재 좌표 지정
# point_x, point_y = 0, 0
# # 배열 내 현재 좌표 위치 1로 표시
# l[point_x][point_y] = 1
#
# # L, R, U, D 순으로 이동할 시 현재 좌표에 더할 값 리스트
# move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# list_len = len(l)
#
# for order in command:
#     if order == 'R':
#         # 다음 이동할 좌표 변수 생성
#         next_point_x, next_point_y = point_x + move[1][0], point_y + move[1][1]
#         # 다음 이동할 좌표가 범위 내에 존재할 경우 이동
#         if 0 <= next_point_x < list_len and 0 <= next_point_y < list_len:
#             # 오른쪽으로 한 칸 이동
#             point_y += 1
#             # 배열 좌표에 이동한 위치 표시
#             l[point_x][point_y] = 1
#         else:
#             # 만약 이동할 좌표가 범위 내에 포함되어 있지 않다면 범위를 벗어나는 것이므로 다음 명령어 루프 수행
#             continue
#     if order == 'L':
#         next_point_x, next_point_y = point_x + move[0][0], point_y + move[0][1]
#         if 0 <= next_point_x < list_len and 0 <= next_point_y < list_len:
#             point_y -= 1
#             l[point_x][point_y] = 1
#         else:
#             continue
#     if order == 'U':
#         next_point_x, next_point_y = point_x + move[2][0], point_y + move[2][1]
#         if 0 <= next_point_x < list_len and 0 <= next_point_y < list_len:
#             point_x -= 1
#             l[point_x][point_y] = 1
#         else:
#             continue
#     if order == 'D':
#         next_point_x, next_point_y = point_x + move[3][0], point_y + move[3][1]
#         if 0 <= next_point_x < list_len and 0 <= next_point_y < list_len:
#             point_x += 1
#             l[point_x][point_y] = 1
#         else:
#             continue
#
# # 현재 좌표가 (1, 1)이 아닌 (0, 0)을 기준으로 하였으므로 각각 1 증가
# print(point_x+1, point_y+1)

# 동빈나 풀이
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)