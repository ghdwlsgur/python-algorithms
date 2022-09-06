import sys


tot = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())


totalMoney = 0
for i in range(0, n):
    money, num = map(int, sys.stdin.readline().split())
    totalMoney += money * num

if tot == totalMoney:
    print("Yes")
else:
    print("No")
