import sys

n, m = map(int, sys.stdin.readline().split())

d = dict()
l = list()
for i in range(n):
    pokemon = sys.stdin.readline().rstrip()
    l.append(pokemon)
    d[pokemon] = int(i) + 1


for i in range(m):
    answer = sys.stdin.readline().rstrip()
    if d.get(answer):
        print(d.get(answer))
    else:
        print(l[int(answer) - 1])
# if d.get(answer):
#     res.append(d.get(answer))
# else:
#     res.append([k for k, v in d.items() if v == int(answer)][0])
