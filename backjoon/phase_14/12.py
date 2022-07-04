
# ! 시간 초과
# import sys
# def factorial(a):
#     if a == 1 or a == 0:
#         return 1
#     return a * factorial(a-1)

# a, b = map(int, sys.stdin.readline().split())
# CB = int(factorial(a) / (factorial(abs(a-b)) * factorial(b)))

# cnt = 0
# l = " ".join(str(CB)).split(" ")
# for i in range(len(l)-1, -1, -1):
#     if i == len(l)-1 and l[i] == '0':
#         cnt += 1
#     else:
#         if l[i] == '0' and l[i+1] == '0':
#             cnt += 1
#         else:
#             break
# print(cnt)

# import sys
# import operator as op
# from functools import reduce
# def nCr(n, r):
#     if n < 1 or r < 0 or n < r:
#         raise ValueError
#     r = min(r, n-r)
#     numerator = reduce(op.mul, range(n, n-r, -1), 1)
#     denominator = reduce(op.mul, range(1, r+1), 1)
#     return numerator // denominator


# a, b = map(int, sys.stdin.readline().split())
# l = " ".join(str(nCr(a, b))).split(" ")

# cnt = 0
# for i in range(len(l)-1, -1, -1):
#     if i == len(l)-1 and l[i] == '0':
#         cnt += 1
#     else:
#         if l[i] == '0' and l[i+1] == '0':
#             cnt += 1
#         else:
#             break
# print(cnt)


# import sys


# def countNum(N, num):
#     count = 0
#     divNum = num
#     while(N >= divNum):
#         count = count + (N // divNum)
#         divNum *= num
#     print(count)
#     return count


# a, b = map(int, sys.stdin.readline().split())

# print(countNum(a, 5))
# print(countNum(b, 5))
# print(countNum(a-b, 5))
# print(countNum(a, 2))
# print(countNum(b, 2))
# print(countNum(a-b, 2))
# print(min(countNum(a, 5) - countNum(b, 5) - countNum(a-b, 5),
#   countNum(a, 2) - countNum(b, 2) - countNum(a-b, 2)))


import sys
a, b = map(int, sys.stdin.readline().split())


def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


print(count_number(a, 2))
# five_count = count_number(a, 5) - count_number(b, 5) - count_number(a - b, 5)
# two_count = count_number(a, 2) - count_number(b, 2) - count_number(a - b, 2)

# print(min(five_count, two_count))
