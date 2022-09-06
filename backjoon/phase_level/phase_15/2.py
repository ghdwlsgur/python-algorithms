
# import sys
# from itertools import combinations

# N, M = map(int, sys.stdin.readline().split())

# cache = []
# for i in range(1, N+1):
#     if M == 1:
#         print(i)
#     else:
#       cache.append(i)
      
# for i in combinations(cache, M):
#   print(*i)
  
# import sys 
# from itertools import combinations 

# N, M = map(int, sys.stdin.readline().split())

# cache = []
# for i in range(1, N+1):
#   if M == 1:
#     print(i)
#   else:
#     cache.append(i)
    
# for i in combinations(cache, M):
#   print(*i)
  

import sys 
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

cache = []
for i in range(1, N+1):
  if M == 1:
    print(i)
  else:
    cache.append(i)
for i in combinations(cache, M):
  print(*i)
  
