# n, m = 8, 8
# 0
# 0
# i = range(0, 8)
# j = range(0, 8)
# row = [0] / 0, 1, 2, 3, 4, 5, 6, 7
# row = [1] / 0, 1, 2, 3, 4, 5, 6, 7
# row = [2] / 0, 1, 2, 3, 4, 5, 6, 7
# ...
# row = [7] / 0, 1, 2, 3, 4, 5, 6, 7

# n, m = 9, 23
# 2 (0, 1)
# 16 (0, 1, 2, ..., 15)
# i = range(0, 8), range(1, 9)
# j = range(0, 8), range(1, 9) ... range(15, 23)
# range(0, 8) * range(0, 8)
# row = [0] / 0, 1, 2, 3, 4, 5, 6, 7
# row = [1] / 0, 1, 2, 3, 4, 5, 6, 7
# row = [2] / 0, 1, 2, 3, 4, 5, 6, 7
# ...
# row = [1] / 0
# range(1, 9) * range


"""
i + j 
[0] 1 [2] 3 [4] 5 [6] 7 [8]
1 [2] 3 [4] 5 [6] 7 [8] 9
[2] 3 [4] 5 [6] 7 [8] 9 [10]
3 4 5 6 7 8 9 10 11
4 5 6 7 8 9 10 11 12 
...

n * m = 9, 9 
[ij]
00 01 02 03 04 05 06 07 08 
10 11 12 13 14 15 16 17 18
20 21 22 23 24 25 26 27 28
30 31 32 33 34 35 36 37 38
40 41 42 43 44 45 46 47 48
50 51 52 53 54 55 56 57 58 
60 61 62 63 64 65 66 67 68 
70 71 72 73 74 75 76 77 78
80 81 82 83 84 85 86 87 88
90 91 92 93 94 95 96 97 98
"""


# n, m = map(int, input().split())

# colors = []
# minimum = []

# for i in range(n):
#     colors.append(input())

# for x in range(n - 7):
#     for y in range(m - 7):
#         a = 0
#         b = 0
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 print(i, j)
#                 if (i + j) % 2 == 0:
#                     if colors[i][j] != 'W':
#                         a += 1
#                     if colors[i][j] != 'B':
#                         b += 1
#                 else:
#                     if colors[i][j] != 'B':
#                         a += 1
#                     if colors[i][j] != 'W':
#                         b += 1
#         minimum.append(a)
#         minimum.append(b)
# print(min(minimum))


# n, m = map(int, input().split())

# colors = []
# m = []
# for i in range(n):
#     colors.append(input())

# for x in range(n - 7):
#     for y in range(m - 7):
#         a = 0
#         b = 0
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 if (i + j) % 2 == 0:
#                     if colors[i][j] != 'W':
#                         a += 1
#                     if colors[i][j] != 'B':
#                         b += 1
#                 else:
#                     if colors[i][j] != 'B':
#                         a += 1
#                     if colors[i][j] != 'W':
#                         b += 1
#         m.append(a)
#         m.append(b)
# print(min(m))

# n, m = map(int, input().split())

# colors = []
# m = []
# for i in range(n):
#     colors.append(input())

# for x in range(n - 7):
#     for y in range(m - 7):
#         a = 0
#         b = 0
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 if (i + j) % 2 == 0:
#                     if colors[i][j] != 'W':
#                         a += 1
#                     if colors[i][j] != 'B':
#                         b += 1
#                 else:
#                     if colors[i][j] != 'B':
#                         a += 1
#                     if colors[i][j] != 'W':
#                         b += 1
#         m.append(a)
#         m.append(b)
# print(min(m))


n, n = map(int, input().split())
colors = []
m = []
for i in range(n):
    colors.append(input())

for x in range(n - 7):
    for y in range(m - 7):
        a = 0
        b = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i + j) % 2 == 0:
                    if colors[i][j] != 'W':
                        a += 1
                    if colors[i][j] != 'B':
                        b += 1
                else:
                    if colors[i][j] != 'B':
                        a += 1
                    if colors[i][j] != 'W':
                        b += 1
        m.append(a)
        m.append(b)
print(min(m))
