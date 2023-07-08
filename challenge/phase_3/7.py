import sys


num = int(input())

for i in range(0, num):
    n = list(map(int, sys.stdin.readline().split()))
    print("Case #%d: %d" % (i+1, int(n[0]) + int(n[1])))
