# import sys
# from math import sqrt


# W, H, X, Y, P = map(int, sys.stdin.readline().split())

# r = H / 2
# circle1 = (X, Y + r)
# circle2 = (X + W, Y + r)

# cnt = 0
# for _ in range(P):
#     x, y = map(int, sys.stdin.readline().split())

#     for x1 in range(circle1[0], circle2[0] + 1):
#         if r >= sqrt(abs(x - x1) ** 2 + abs(y - (Y + r)) ** 2):
#             cnt += 1
#             break

# print(cnt)

import sys
from math import sqrt


W, H, X, Y, P = map(int, sys.stdin.readline().split())

r = H / 2
circle1 = (X, Y + r)
circle2 = (X + W, Y + r)
cnt = 0
for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())
    for x1 in range(circle1[0], circle2[0] + 1):
        if r >= sqrt(abs(x - x1) ** 2 + abs(y - (Y + r)) ** 2):
            cnt += 1
            break
print(cnt)
