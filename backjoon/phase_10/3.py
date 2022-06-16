# 5
# 55 185 k 1 => 2
# 58 183 k 1 => 2
# 88 186 k 0 => 1
# 60 175 k 1 => 2
# 46 155 k 4 => 5


# l = []
# for i in range(0, int(input())):
#     weight, height = map(int, input().split())
#     l.append((weight, height))

# for i in l:
#     rank = 1
#     for j in l:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=" ")

# l = []
# for i in range(0, int(input())):
#     weight, height = map(int, input().split())
#     l.append((weight, height))

# for i in l:
#     rank = 1
#     for j in l:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=" ")

# l = []
# for i in range(0, int(input())):
#     weight, height = map(int, input().split())
#     l.append((weight, height))

# for i in l:
#     rank = 1
#     for j in l:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=" ")

# l = []
# for i in range(0, int(input())):
#     weight, height = map(int, input().split())
#     l.append((weight, height))

# for i in l:
#     rank = 1
#     for j in l:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=" ")

# l = []
# for i in range(0, int(input())):
#     weight, height = map(int, input().split())
#     l.append((weight, height))

# for i in l:
#     rank = 1
#     for j in l:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=" ")


l = []
for i in range(0, int(input())):
    weight, height = map(int, input().split())
    l.append((weight, height))

for i in l:
    rank = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
