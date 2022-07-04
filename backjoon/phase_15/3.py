import sys
from itertools import product


N, M = map(int, sys.stdin.readline().split())

cache = []
for i in range(1, N+1):
    if M == 1:
        print(i)
    else:
        cache.append(i)

for i in product(cache, repeat=M):
    print(*i)
