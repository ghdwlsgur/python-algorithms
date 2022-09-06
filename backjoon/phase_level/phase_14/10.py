
import sys

for i in range(int(sys.stdin.readline().rstrip())):

    wear = dict()
    for j in range(int(sys.stdin.readline().strip())):
        input = list(sys.stdin.readline().split())
        if input[1] in wear:
            wear[input[1]].append(input[0])
        else:
            wear[input[1]] = [input[0]]

    cnt = 1
    for k in wear:
        cnt *= (len(wear[k]) + 1)
    print(cnt - 1)
