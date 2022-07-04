import sys 
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())

cache = []
for i in range(1, N+1):
  if M == 1:
    print(i)
  else:
    cache.append(i)
    
for i in combinations_with_replacement(cache, M):
  print(*i)