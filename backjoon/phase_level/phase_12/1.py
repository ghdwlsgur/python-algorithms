

# ! 시간 초과
# import sys
# n = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))

# correct = []
# for i in range(int(sys.stdin.readline()) + 1):
#     if i == 0:
#         correct = list(map(int, sys.stdin.readline().split()))
#     else:
#         print(l.count(correct[i-1]), end=" ")


# 이진탐색 활용
# import sys
# def bs(array, target, start, end):
#     while start <= end:
#         m = (start + end) // 2
#         if array[m] == target:
#             return 1
#         elif array[m] > target:
#             end = m - 1
#         else:
#             start = m + 1
#     return 0
# n = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# answer = list(map(int, sys.stdin.readline().split()))
# l.sort()
# for i in answer:
#     print(bs(l, i, 0, n-1), end=" ")

import sys
n = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = ''

for i in range(m):
    if arr[i] in n_set:
        answer += "1 "
    else:
        answer += "0 "

print(answer[:-1])
