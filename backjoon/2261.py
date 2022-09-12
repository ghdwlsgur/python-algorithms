# import sys
# from math import sqrt

# # 가장 가까운 두 점
# l = []
# for _ in range(int(sys.stdin.readline().rstrip())):
#     a, b = map(int, sys.stdin.readline().split())
#     l.append((a, b))
# l = list(set(l))

# distance = set()
# for i in range(0, len(l)):
#     for j in range(i + 1, len(l)):
#         distance.add(sqrt(abs(l[i][0] - l[j][0]) **
#                      2 + abs(l[i][1] - l[j][1]) ** 2))
# print(int(min(distance) ** 2))

"""
import sys
num = int(sys.stdin.readline().rstrip())
# x축 정렬
l = sorted([list(map(int, sys.stdin.readline().split())) for i in range(num)])


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def friendOfDot(start, end):
    # 점이 하나만 존재할 경우
    if start == end:
        return float('inf')

    # 점이 두 개 존재할 경우 (두 점 사이의 거리 반환)
    if end - start == 1:
        return dist(l[start], l[end])

    # 분할 정복 알고리즘
    mid = (start + end) // 2  # 중간 인덱스
    minDist = min(friendOfDot(start, mid), friendOfDot(mid, end))

    target_l = []
    for i in range(start, end+1):
        if (l[mid][0] - l[i][0]) ** 2 < minDist:
            target_l.append(l[i])

    target_l.sort(key=lambda x: x[1])

    # y축 정렬
    t = len(target_l)
    for i in range(t - 1):
        for j in range(i + 1, t):
            if (target_l[i][1] - target_l[j][1]) ** 2 < minDist:
                minDist = min(minDist, dist(target_l[i], target_l[j]))
            else:
                break
    return minDist
print(friendOfDot(0, num-1))
"""
