
a, b = map(int, input().split())
l = list(map(int, input().split()))

res = []
for i in range(0, len(l)):
    if l[i] < b:
        res.append(l[i])

print(*res)
