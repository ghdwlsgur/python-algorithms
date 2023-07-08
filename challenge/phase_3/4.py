
import sys

tot = int(input())
n = int(input())

sum = 0
for i in range(0, n):
    num = list(map(int, sys.stdin.readline().split()))
    sum += num[0] * num[1]

if sum != tot:
    print("No")
else:
    print("Yes")
