
import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
find_num = int(input())

cnt = 0
for i in range(0, n):
    if l[i] == find_num:
        cnt += 1

print(cnt)
