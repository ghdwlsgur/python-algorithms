

n, k = map(int, input().split())

l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)

res = 0
for i in range(n):
    if k % l[i] < l[i]:
        res += k // l[i]
        k = k % l[i]

print(res)
