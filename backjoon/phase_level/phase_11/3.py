
import sys
n = int(input())

l = [0] * 10001
for i in range(n):
    l[int(sys.stdin.readline())] += 1

for i in range(10001):
    if l[i] != 0:
        # correct
        for j in range(0, l[i]):
            print(i)
        # leak memory
        # print("\n".join([str(i)]*l[i]))
