
import sys
# ! version 1
# Todo: 108ms
# n = int(sys.stdin.readline())
# l = []
# for _ in range(n):
#     a = sys.stdin.readline().split()[0]
#     l.append(a)
# l = sorted(list(set(l)))
# l.sort(key=len)
# for a in l:
#     print(a)

# ! version 2: short coding
# Todo: 128ms
l = [sys.stdin.readline().split()[0] for i in range(int(sys.stdin.readline()))]
l = sorted(list(set(l)))
l.sort(key=len)

for i in l:
    print(i)
