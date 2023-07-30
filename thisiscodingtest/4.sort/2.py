
n = int(input())

l = []
for i in range(n):
    l.append(input().split())

for i in sorted(l, key=lambda l: int(l[1])):
    print(i[0], end=' ')
