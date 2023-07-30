

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

for i in sorted(l, reverse=True):
    print(i, end=' ')