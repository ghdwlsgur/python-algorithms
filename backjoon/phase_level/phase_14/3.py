
# import sys
# a, b = map(int, sys.stdin.readline().split())


# for i in range(min(a, b), 0, -1):
#     if (a % i == 0) and (b % i == 0):
#         print(i)
#         break

# for i in range(max(a, b), (a * b)+1, max(a, b)):
#     if (i % a == 0) and (i % b == 0):
#         print(i)
#         break

import sys
a, b = map(int, sys.stdin.readline().split())

for i in range(min(a, b), 0, -1):
    if (a % i == 0) and (b % i == 0):
        print(i)
        break

for i in range(max(a, b), (a * b) + 1, max(a, b)):
    if (i % a == 0) and (i % b == 0):
        print(i)
        break
