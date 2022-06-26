

import sys
n, m = map(int, sys.stdin.readline().split())

dic = dict()
for i in range(n):
    dic[sys.stdin.readline().rstrip()] = 1

count = 0
res = []
for i in range(m):
    answer = sys.stdin.readline().rstrip()
    if dic.get(answer):
        res.append(answer)
        count += 1

res.sort()
print(count)
print(*res, sep="\n")
