
# sort() vs sorted()
# ! correct 1
# b = sorted(list(set(a)))
# ! None
# b = list(set(a)).sort()
# ! correct 2
# b = list(set(a))
# b.sort()
# https://minorman.tistory.com/16

# ! 시간 초과
# import sys
# n = int(sys.stdin.readline())
# l1 = []

# for i in range(n):
#     l1.append(int(sys.stdin.readline()))

# l1 = sorted(l1)
# l2 = sorted(list(set(l1)))

# print(round(sum(l1) / n))
# print(l1[(n - 1) // 2])
# k = l1[-1] - l1[0]

# while l1 != l2:
#     for i in l2:
#         if i in l1:
#             l1.remove(i)
#     for i in l2:
#         if i not in l1:
#             l2.remove(i)

# if len(l1) == 1:
#     print(l1[0])
# else:
#     print(l1[1])
# print(k)


# import sys
# from collections import Counter
# n = int(sys.stdin.readline())
# l = list()
# for _ in range(n):
#     l.append(int(sys.stdin.readline()))
# l.sort()
# print(round(sum(l) / n))
# print(l[int(n / 2)])

# mode = Counter(l).most_common()

# if len(mode) == 1:
#     print(mode[0][0])
# elif mode[0][1] == mode[1][1]:
#     print(mode[1][0])
# else:
#     print(mode[0][0])

# print(l[-1] - l[0])


# import sys
# from collections import Counter
# n = int(sys.stdin.readline())
# l = list()
# for _ in range(n):
#     l.append(int(sys.stdin.readline()))
# l.sort()
# print(round(sum(l) / n))
# print(l[int(n / 2)])

# mode = Counter(l).most_common()
# if len(mode) == 1:
#     print(mode[0][0])
# elif mode[0][1] == mode[1][1]:
#     print(mode[1][0])
# else:
#     print(mode[0][0])
# print(l[-1]-l[0])


import sys
from collections import Counter
n = int(sys.stdin.readline())
l = list()
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
print(round(sum(l) / n))
print(l[int(n/2)])

m = Counter(l).most_common()
if len(m) == 1:
    print(m[0][0])
elif m[0][1] == m[1][1]:
    print(m[1][0])
else:
    print(m[0][0])
print(l[-1] - l[0])
