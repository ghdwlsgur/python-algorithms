

import sys
dic_a = dict()
dic_b = dict()
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if dic_a.get(a):
        dic_a[a] += 1
    else:
        dic_a[a] = 1
        
    if dic_b.get(b):
        dic_b[b] += 1
    else:
        dic_b[b] = 1

print([k for k, v in dic_a.items() if v == 1][0], end=" ")
print([k for k, v in dic_b.items() if v == 1][0])
