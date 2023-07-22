import sys

l = []
for i in range(9):
    l.append(list(map(int, sys.stdin.readline().split())))


a, b = 0, 0
max = 0
for i in range(9):
    for j in range(len(l)):
        if l[i][j] >= max:
            max = l[i][j]
            a = i+1
            b = j+1

print(max)
print(a, b)