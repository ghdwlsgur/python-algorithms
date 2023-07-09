n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(0, 23):
    l.append(0)


for i in range(0, n):
    l[a[i]-1] += 1

print(*l)
