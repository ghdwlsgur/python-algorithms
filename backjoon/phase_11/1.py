# n = int(input())

# l = []
# for i in range(n):
#     l.append(int(input()))

# l.sort()
# for i in l:
#     print(i)

import sys
n = int(input())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

for i in sorted(l):
    print(i)
