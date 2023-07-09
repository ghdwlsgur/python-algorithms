
# l = []
# for i in range(19):
#     l.append([])
#     for j in range(19):
#         l[i].append(0)

l = []
for i in range(19):
    d = list(map(int, input().split()))
    l.append(d)


for i in range(0, int(input())):
    a, b = map(int, input().split())
    for i in range(19):
        if l[a-1][i] == 0:
            l[a-1][i] = 1
        else:
            l[a-1][i] = 0
    for i in range(19):
        if l[i][b-1] == 0:
            l[i][b-1] = 1
        else:
            l[i][b-1] = 0

for i in l:
    print(*i)
