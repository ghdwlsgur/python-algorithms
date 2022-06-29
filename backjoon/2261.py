import sys
from math import sqrt

# 가장 가까운 두 점
l = []
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))

distance = set()
for i in range(0, len(l)):
  for j in range(i + 1, len(l)):
    distance.add(sqrt(abs(l[i][0] - l[j][0]) ** 2 + abs(l[i][1] - l[j][1]) ** 2))
print(int(min(distance) ** 2))
    