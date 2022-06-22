
# ! version 1
# ! 시간 초과
# import sys
# l = []
# N = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))

# sorted_l = sorted(list(set(l)))

# for i in sorted_l:
#     for j in l:
#         if i == j:
#             l[l.index(i)] = sorted_l.index(i)

# print(*l, sep=" ")

# ! version 2
# ! 시간 초과
# import sys
# l = []
# N = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))

# sorted_l = sorted(list(set(l)))

# for i in range(0, len(sorted_l)):
#     for j in range(0, len(l)):
#         if sorted_l[i] == l[j]:
#             l[j] = i

# print(*l, sep=" ")

# ! version 3
# import sys
# l = []
# N = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))

# sorted_l = sorted(list(set(l)))
# dic = {sorted_l[i]: i for i in range(len(sorted_l))}

# for i in l:
#     print(dic[i], end=' ')


# import sys
# N = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))

# sorted_l = sorted(list(set(l)))
# dic = {sorted_l[i]: i for i in range(0, len(sorted_l))}

# for i in l:
#     print(dic[i], end=' ')

import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rstrip().split()))

rank = 0
min_n = min(l)
dic = {}

for i in sorted(l):
    if i > min_n:
        min_n = i
        rank += 1
    dic[i] = rank

print(*[dic[i] for i in l])
