import sys

l = []
max = 0
for i in range(5):
    str = list(sys.stdin.readline().rstrip())
    l.append(str)
    if max < len(str):
        max = len(str)

for i in range(5):
    if len(l[i]) < max:
        cnt = max - len(l[i])
        for _ in range(cnt):
            l[i].append("")

for i in range(max):
    for j in range(len(l)):
        print(l[j][i], end='')