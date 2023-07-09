

l = []
for i in range(19):
    l.append([])
    for j in range(19):
        l[i].append(0)


for i in range(0, int(input())):
    a, b = map(int, input().split())
    l[a-1][b-1] = 1


for i in l:
    print(*i)
