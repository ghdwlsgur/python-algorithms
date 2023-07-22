import sys

input = sys.stdin.readline()
n, m = map(int, input.split())

l = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    l.append(a)

ll = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    ll.append(a)

for i in range(n):
    for j in range(m):
        print(int(l[i][j]) + int(ll[i][j]), end=' ')
    print()
