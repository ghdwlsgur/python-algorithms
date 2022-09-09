# import sys
# n = int(sys.stdin.readline().rstrip())
# d = [0 for _ in range(n+1)]

# for i in range(2, n + 1):
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[n])

"""
0 -> 0
1 -> 0
2 -> 1
3 -> 1
4 -> 2 
"""

import sys
import math


def solve():
    n = int(sys.stdin.readline().rstrip())
    arr = [0, 0, 1, 1, 2]

    for i in range(5, n + 1):
        a, b, c = math.inf, math.inf, arr[i - 1]
        if i % 3 == 0:
            a = arr[i // 3]
        if i % 2 == 0:
            b = arr[i // 2]
        arr.append(1 + min(a, b, c))
    print(arr[n])


solve()


def test():
    n = int(sys.stdin.readline().rstrip())
    arr = [0, 0, 1, 1, 2]

    for i in range(5, n + 1):
        a, b, c = math.inf, math.inf, arr[i - 1]
        if i % 3 == 0:
            a = arr[i // 3]
        if i % 2 == 0:
            b = arr[i // 2]
        arr.append(1 + min(a, b, c))
    print(arr[n])


test()
