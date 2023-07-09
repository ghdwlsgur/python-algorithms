# ldxy
# 길이, 방향, x(세로), y(가로)

a, b = map(int, input().split())
n = int(input())

ll = []
for i in range(a):
    ll.append([])
    for j in range(b):
        ll[i].append(0)


for i in range(n):
    l, d, x, y = map(int, input().split())
    ll[x-1][y-1] = 1

    for i in range(l):
        if d == 0:
            ll[x-1][y-1+i] = 1
        if d == 1:
            ll[x-1+i][y-1] = 1

for i in ll:
    print(*i)
