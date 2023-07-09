

a, b, c = map(int, input().split())

cnt = 0
for l in range(0, a):
    for m in range(0, b):
        for n in range(0, c):
            print(l, m, n)
            cnt += 1


print(cnt)
