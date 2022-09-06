
import sys
# version 1
# n = int(sys.stdin.readline())
# l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# l.sort(key=lambda x: (x[1], x[0]))
# print(l)

# l = [list(map(int, sys.stdin.readline().split()))
#      for i in range(int(sys.stdin.readline()))]
# l.sort(key=lambda x: (x[1], x[0]))
# for a, b in l:
#     print(a, b)

# l = [list(map(int, sys.stdin.readline().split()))
#      for i in range(int(sys.stdin.readline()))]
# l.sort(key=lambda x: (x[1], x[0]))
# for a, b in l:
#     print(a, b)

# l = [list(map(int, sys.stdin.readline().split()))
#      for i in range(int(sys.stdin.readline()))]
# l.sort(key=lambda x: (x[1], x[0]))
# for a, b in l:
#     print(a, b)

# l = [list(map(int, sys.stdin.readline().split()))
#      for i in range(int(sys.stdin.readline()))]
# l.sort(key=lambda x: (x[1], x[0]))
# for a, b in l:
#     print(a, b)

l = [list(map(int, sys.stdin.readline().split()))
     for i in range(sys.stdin.readline())]
l.sort(key=lambda x: (x[1], x[0]))
for a, b in l:
    print(a, b)
