# from math import sqrt, gcd
# import sys
# from math import gcd, sqrt

# n = int(sys.stdin.readline().rstrip())
# input = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

# l = []
# for i in range(1, len(input)):
#     l.append(abs(input[i] - input[i-1]))

# target = l[0]
# for i in range(1, len(input) - 1):
#     target = gcd(target, l[i])


# result = []
# for i in range(1, int(sqrt(target)) + 1):
#     if target % i == 0:
#         if i ** 2 == target:
#             result.append(i)
#         else:
#             result += [i, target // i]

# result.remove(1)

# for i in sorted(result):
#     print(i, end=" ")


# n = int(sys.stdin.readline().rstrip())
# input = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

# l = []
# for i in range(1, len(input)):
#     l.append(abs(input[i] - input[i-1]))

# target = l[0]
# for i in range(1, len(input)-1):
#     target = gcd(target, l[1])

# result = []
# for i in range(1, int(sqrt(target)) + 1):
#     if target % i == 0:
#         if i ** 2 == target:
#             result.append(i)
#         else:
#             result += [i, target // i]
# result.remove(1)

# for i in sorted(result):
#     print(i, end=" ")


# n = int(sys.stdin.readline().rstrip())
# input = sorted([int(sys.stdin.readline().rstrip())] for _ in range(n))

# l = []
# for i in range(1, len(input)):
#     l.append(abs(input[i] - input[i-1]))

# target = l[0]
# for i in range(1, len(input)-1):
#     target = gcd(target, l[i])

# result = []
# for i in range(1, int(sqrt(target)) + 1):
#     if target % i == 0:
#         if i ** 2 == target:
#             result.append(i)
#         else:
#             result += [i, target // i]
# result.remove(1)

# for i in sorted(result):
#     print(i, end=" ")


# import sys
# from math import sqrt, gcd
# n = int(sys.stdin.readline().rstrip())
# input = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# l = []
# # 입력받은 수의 차이를 구한다.
# for i in range(1, len(input)):
#     l.append(abs(input[i] - input[i - 1]))

# target = l[0]
# # 값들의 최대공약수를 구한다.
# for i in range(1, len(input) - 1):
#     target = gcd(target, l[i])

# result = []
# # 최대공약수의 제곱근까지를 벙뮈로 하여 약수를 추출한다.
# for i in range(1, int(sqrt(target)) + 1):
#     if target % i == 0:
#         if i ** 2 == target:
#             result.append(i)
#         else:
#             result += [i, target // i]
# result.remove(1)

# for i in result:
#     print(i, end=" ")


# n = int(sys.stdin.readline().rstrip())
# input = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# l = []
# for i in range(1, len(input)):
#     l.append(input[i] - input[i - 1])

# target = l[0]
# for i in range(1, len(input) - 1):
#     target = gcd(target, l[i])

# result = []
# for i in range(1, int(sqrt(target)) + 1):
#     if target % i == 0:
#         if i ** 2 == target:
#             result.append(i)
#         else:
#             result += [i, target // i]
# result.remove(1)

# for i in sorted(result):
#     print(i, end=" ")

import sys
from math import sqrt, gcd

n = int(sys.stdin.readline().rstrip())
input = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
l = []
# 입력받은 수의 차이를 구한다.
for i in range(1, len(input)):
    l.append(input[i] - input[i - 1])

target = l[0]
# 값들의 최대공약수를 구한다.
for i in range(1, len(input) - 1):
    target = gcd(target, l[i])

result = []
# 최대공약수의 제곱근까지를 벙뮈로 하여 약수를 추출한다.
for i in range(1, int(sqrt(target)) + 1):
    if target % i == 0:
        if i ** 2 == target:
            result.append(i)
        else:
            result += [i, target // i]
result.remove(1)

for i in sorted(result):
    print(i, end=" ")



