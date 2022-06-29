"""
총 진입 / 이탈 횟수가 추가되는 경우는 
출발점이나 도착점이 행성 내부에 위치한 경우 (출발점과 행성 중심과의 거리가 행성 반지름보다 작은 경우)
단, 출발점과 도착점이 모두 행성 내부에 위치해 있다면 (행성 중심과의 거리가 모두 행성의 반지름보다 작은 경우)
총 진입/이탈 횟수 = 0
"""

# import sys
# from math import sqrt

# n = int(sys.stdin.readline().rstrip())

# for _ in range(n):
#     start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
#     t = int(sys.stdin.readline())

#     cnt = 0
#     for _ in range(t):
#         planet_x, planet_y, planet_r = map(int, sys.stdin.readline().split())
#         distance_with_start = sqrt(
#             abs(start_x - planet_x) ** 2 + abs(start_y - planet_y) ** 2)
#         distance_with_end = sqrt(abs(end_x - planet_x)
#                                  ** 2 + abs(end_y - planet_y) ** 2)

#         if planet_r > distance_with_start and planet_r > distance_with_end:
#             pass
#         elif planet_r > distance_with_start:
#             cnt += 1
#         elif planet_r > distance_with_end:
#             cnt += 1
#     print(cnt)


# import sys
# from math import sqrt
# n = int(sys.stdin.readline().rstrip())

# for _ in range(n):
#     start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
#     t = int(sys.stdin.readline())

#     cnt = 0
#     for _ in range(t):
#         planet_x, planet_y, r = map(int, sys.stdin.readline().split())
#         distance_with_start = sqrt(
#             abs(start_x - planet_x) ** 2 + abs(start_y - planet_y) ** 2)
#         distance_with_end = sqrt(abs(end_x - planet_x)
#                                  ** 2 + abs(end_y - planet_y) ** 2)

#         if r > distance_with_start and r > distance_with_end:
#             pass
#         elif r > distance_with_start:
#             cnt += 1
#         elif r > distance_with_end:
#             cnt += 1
#     print(cnt)

import sys
from math import sqrt

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    t = int(sys.stdin.readline().rstrip())
    cnt = 0
    for _ in range(t):
        planet_x, planet_y, r = map(int, sys.stdin.readline().split())

        distance_with_start = sqrt(
            abs(start_x - planet_x) ** 2 + abs(start_y - planet_y) ** 2)
        distance_with_end = sqrt(abs(end_x - planet_x)
                                 ** 2 + abs(end_y - planet_y) ** 2)

        if r > distance_with_start and r > distance_with_end:
            pass
        elif r > distance_with_start:
            cnt += 1
        elif r > distance_with_end:
            cnt += 1

    print(cnt)
