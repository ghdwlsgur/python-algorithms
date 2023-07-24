
# 나의 풀이
# # 입력 변수
# loc = list(input())
#
# # 입력 변수의 행과 열을 (0, 0)을 기준으로 설정
# x, y = int(ord(loc[0]) - ord('a')), int(loc[1]) - 1
#
# # 8 X 8 좌표 평면 리스트 생성
# l = [[0 for _ in range(8)] for _ in range(8)]
#
# # 현재 좌표에서 말을 둘 수 있는 곳으로 이동하기 위해 증감할 수 있는 경우의 수
# move = [(2, -1), (2, 1), (1, -2), (-2, 1), (1, 2), (-1, 2), (-1, -2), (-2, -1)]
#
# # 카운트 변수
# cnt = 0
#
# # 이동할 수 있는 각 경우의 수를 모두 조합
# for v in move:
#     # 말을 둘 수 있는 위치가 8 X 8 범위 내에 포함된 경우만 카운트
#     next_x, next_y = x+v[0], y+v[1]
#     if next_x < 0 or next_x > 8 or next_y < 0 or next_y > 8:
#         continue
#     else:
#         cnt += 1
#
# print(cnt)

# 동빈나 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)


