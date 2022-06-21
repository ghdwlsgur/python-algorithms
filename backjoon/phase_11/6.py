
# ! version 1
# l = []
# for _ in range(int(input())):
#     l.append(list(map(int, input().split())))
# l.sort()
# for a, b in l:
#     print(a, b)

# ! version 2
# N = int(sys.stdin.readline())
# M = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# M.sort()
# for a, b in M:
#     print(a, b)

# ! version 3
# n = int(sys.stdin.readline())
# l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# l.sort()
# for a, b in l:
#     print(a, b)

import sys
l = sorted([list(map(int, sys.stdin.readline().split()))
           for i in range(int(sys.stdin.readline()))])
for i in l:
    print(l[i][0], l[i][1])
