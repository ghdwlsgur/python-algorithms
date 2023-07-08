import sys


num = int(input())

for i in range(0, num):
    n = list(map(int, sys.stdin.readline().split()))
    print(n[0]+n[1])
