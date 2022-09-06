# import sys
# n, m = map(int, sys.stdin.readline().split())

# str = ""
# total = 0
# for _ in range(n):
#     str += sys.stdin.readline().rstrip()
#     str += " "

# l = str.rstrip().split(" ")
# for i in range(m):
#     a = sys.stdin.readline().rstrip()
#     if a in l:
#         total += 1
# print(total)

import sys
n, m = map(int, input().split())
dic = dict()
count = 0

for _ in range(n):
    str = sys.stdin.readline().rstrip()
    dic[str] = True

for _ in range(m):
    a = sys.stdin.readline().rstrip()
    if dic.get(a):
        count += 1
print(count)
