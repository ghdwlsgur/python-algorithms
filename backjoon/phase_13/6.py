# import sys
# from math import sqrt


# n = int(sys.stdin.readline().rstrip())
# x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

# range1_co = []
# range2_co = []
# range1_checkpoint = []
# range2_checkpoint = []


# def endpointLocation(x, y, r, checkpoint):
#     range_co = []
#     for a in range(x, checkpoint[0][0]+1):
#         for b in range(y, checkpoint[0][1]+1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[1][0]-1, -1):
#         for b in range(y, checkpoint[1][1]+1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[2][0]-1, -1):
#         for b in range(y, checkpoint[2][1]-1, -1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[3][0]+1):
#         for b in range(y, checkpoint[3][1]-1, -1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     return range_co


# test1 = []
# test2 = []
# if x1 == x2 and y1 == y2 and r1 == r2:
#     print(-1)
# elif x1 == x2 and y1 == y2 and r1 != r2:
#     print(0)
# else:
#     range1_checkpoint = [(x1 + r1, y1 + r1), (x1 - r1, y1 + r1),
#                          (x1 - r1, y1 - r1), (x1 + r1, y1 - r1)]
#     range2_checkpoint = [(x2 + r2, y2 + r2), (x2 - r2, y2 + r2),
#                          (x2 - r2, y2 - r2), (x2 + r2, y2 - r2)]
#     test1 = endpointLocation(x1, y1, r1, range1_checkpoint)
#     test2 = endpointLocation(x2, y2, r2, range2_checkpoint)

# 1사분면
# for x in range(x1, range1_checkpoint[0][0]+1):
#     for y in range(y1, range1_checkpoint[0][1]+1):
#         co_between_x1y1 = sqrt((abs(x1 - x) ** 2) + (abs(y1 - y) ** 2))
#         if co_between_x1y1 == r1:
#             range1_co.append((x, y))
# # 2사분면
# for x in range(x1, range1_checkpoint[1][0]-1, -1):
#     for y in range(y1, range1_checkpoint[1][1]+1):
#         co_between_x1y1 = sqrt((abs(x1 - x) ** 2) + (abs(y1 - y) ** 2))
#         if co_between_x1y1 == r1:
#             range1_co.append((x, y))
# # 3사분면
# for x in range(x1, range1_checkpoint[2][0]-1, -1):
#     for y in range(y1, range1_checkpoint[2][1]-1, -1):
#         co_between_x1y1 = sqrt((abs(x1 - x) ** 2) + (abs(y1 - y) ** 2))
#         if co_between_x1y1 == r1:
#             range1_co.append((x, y))
# # 4사분면
# for x in range(x1, range1_checkpoint[3][0]+1):
#     for y in range(y1, range1_checkpoint[3][1]-1, -1):
#         co_between_x1y1 = sqrt((abs(x1 - x) ** 2) + (abs(y1 - y) ** 2))
#         if co_between_x1y1 == r1:
#             range1_co.append((x, y))

# # 1사분면
# for x in range(x2, range2_checkpoint[0][0]+1):
#     for y in range(y2, range2_checkpoint[0][1]+1):
#         co_between_x2y2 = sqrt((abs(x2 - x) ** 2) + (abs(y2 - y) ** 2))
#         if co_between_x2y2 == r2:
#             range2_co.append((x, y))
# # 2사분면
# for x in range(x2, range2_checkpoint[1][0]-1, -1):
#     for y in range(y2, range2_checkpoint[1][1]+1):
#         co_between_x2y2 = sqrt((abs(x2 - x) ** 2) + (abs(y2 - y) ** 2))
#         if co_between_x2y2 == r2:
#             range2_co.append((x, y))
# # 3사분면
# for x in range(x2, range2_checkpoint[2][0]-1, -1):
#     for y in range(y2, range2_checkpoint[2][1]-1, -1):
#         co_between_x2y2 = sqrt((abs(x2 - x) ** 2) + (abs(y2 - y) ** 2))
#         if co_between_x2y2 == r2:
#             range2_co.append((x, y))
# # 4사분면
# for x in range(x2, range2_checkpoint[2][0]+1):
#     for y in range(y2, range2_checkpoint[2][1]-1, -1):
#         co_between_x2y2 = sqrt((abs(x2 - x) ** 2) + (abs(y2 - y) ** 2))
#         if co_between_x2y2 == r2:
#             range2_co.append((x, y))
# cnt = 0
# for i in list(set(test1)):
#     for j in list(set(test2)):
#         if i == j:
#             cnt += 1

# print(cnt)


# ! 시간초과
# import sys
# from math import sqrt
# """
# 원점으로부터 반지름의 길이만큼 최대 좌표수를 구한 후
# 구한 좌표와 원점 좌표 사이에 위치한 좌표와 원점으로부터의 거리를 구하여
# 이 거리가 반지름의 길이와 동일할 경우 원의 끝점에 위치한 좌표이다.

# 즉 원점을 기준으로 사각형의 모서리를 포인트 기점으로 하여
# 분할하여 좌표를 구한다.
# """


# def endpointLocation(x, y, r, checkpoint):
#     range_co = []
#     for a in range(x, checkpoint[0][0]+1):
#         for b in range(y, checkpoint[0][1]+1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[1][0]-1, -1):
#         for b in range(y, checkpoint[1][1]+1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[2][0]-1, -1):
#         for b in range(y, checkpoint[2][1]-1, -1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     for a in range(x, checkpoint[3][0]+1):
#         for b in range(y, checkpoint[3][1]-1, -1):
#             co_between_xy = sqrt((abs(x - a) ** 2) + (abs(y - b) ** 2))
#             if co_between_xy == r:
#                 range_co.append((a, b))
#     return range_co


# n = int(sys.stdin.readline().rstrip())


# range1_co = []
# range2_co = []
# for i in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
#     if (x1 == x2 and y1 == y2 and r1 == r2) or abs(r1 - r2) == (sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))):
#         print(-1)
#     elif x1 == x2 and y1 == y2 and r1 != r2:
#         print(0)
#     else:
#         range1_checkpoint = [(x1 + r1, y1 + r1), (x1 - r1, y1 + r1),
#                              (x1 - r1, y1 - r1), (x1 + r1, y1 - r1)]
#         range2_checkpoint = [(x2 + r2, y2 + r2), (x2 - r2, y2 + r2),
#                              (x2 - r2, y2 - r2), (x2 + r2, y2 - r2)]
#         range1_co = endpointLocation(x1, y1, r1, range1_checkpoint)
#         range2_co = endpointLocation(x2, y2, r2, range2_checkpoint)

#         cnt = 0

#         print(range1_co)
#         print(range2_co)
#         for i in list(set(range1_co)):
#             for j in list(set(range2_co)):
#                 if i == j:
#                     cnt += 1
#         print(cnt)


from math import sqrt
import sys

n = int(sys.stdin.readline().rstrip())
"""
첫 번째 조건: 두 원의 원점 사이의 거리가 동일하고 반지름이 같을 때 (완전히 겹칠 때)
두 번째 조건: 
- 두 원의 반지름의 차이가 두 원점 사이의 거리와 동일할 떄 (내접)
- 두 원의 반지름의 합이 두 원의 원점 사이의 거리와 동일할 때 (외접)
세 번째 조건:
- 두 원의 원점 사이의 거리가 두 원의 반지름의 차이보다 크고 두 원의 반지름의 합보다 작을 때 (두 점으로 겹칠 때)

"""
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)


# from math import sqrt
# import sys

# n = int(sys.stdin.readline().rstrip())

# for _ in range(n):
#   x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
#   distance = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
#   if distance == 0 and r1 == r2:
#     print(-1)
#   elif abs(r1 - r2) == distance or r1 + r2 == distance:
#     print(1)
#   elif abs(r1 - r2) < distance < (r1 + r2):
#     print(2)
#   else:
#     print(0)

# n = int(sys.stdin.readline().rstrip())

# for _ in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
#     distance = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
#     if distance == 0 and r1 == r2:
#         print(-1)
#     elif abs(r1 - r2) == distance or r1 + r2 == distance:
#         print(1)
#     elif abs(r1 - r2) < distance < (r1 + r2):
#         print(2)
#     else:
#         print(0)
