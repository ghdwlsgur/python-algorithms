import sys

input = sys.stdin.readline

n = int(input())
a = ["9", "4", "8", "6", "5", "3", "7"]

sum = 0
for i in range(n):
    alphabet = input().rstrip()
    ll = list(alphabet)
    str = ""
    for j in ll:
        str += a[int(ord(j))-65]
    sum += int(str)

print(sum)





