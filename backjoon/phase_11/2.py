from audioop import reverse
import sys
n = int(input())

l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

for i in sorted(l):
    print(i)


# for i in sorted(l, reverse=True):
#     print(i)
