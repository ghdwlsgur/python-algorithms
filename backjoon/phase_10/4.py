

# n, m = map(int, input().split())

# l = []
# for i in range(n):
#     for j in range(m):
#         l.append(input())
#     l.append(" ")

# print("".join(l).split(" "))


n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(input())
    l.append(" ")
    if len(l[i * 2]) != m:
        break
l.pop()

cnt = 0
res = 0
for row in "".join(l).split(" "):
    for j in range(0, len(row)):
        if cnt == 0 and row[0] == 'W':
            if cnt % 2 == 0:
                if row[j % 2 == 0] != 'W':
                    print("j", j)
                    print("cnt", cnt)
                    print("j % 2", j % 2)
                    print(row[j % 2 == 0])
                    res += 1
                elif row[j % 2 == 1] != 'B':
                    res += 1
            else:
                if row[j % 2 == 0] != 'B':
                    res += 1
                elif row[j % 2 == 1] != 'W':
                    res += 1
        cnt += 1
        # if cnt == 0 and row[0] == "B":
        #     print(j)

print(res)
# WBWBWBWB [0]
# BWBWBWBW [1]

# 0 [1] 2 [3] 4 [5] 6 [7]
# i = 0 len = 2 check = 0
# i = 1 len = 4 check = 2
# i = 2 len = 6 check = 4
# i = 3 len = 8 check = 6

# print("".join(l).split(" "))
