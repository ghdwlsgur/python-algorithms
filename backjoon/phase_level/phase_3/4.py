import sys

num = int(input())

for i in range(0, num):
    n = sys.stdin.readline().split()
    print(int(n[0]) + int(n[1]))
