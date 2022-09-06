
# summary
# a = 10 b = 12
"""
10 % 12 == 10
12 % 10 == 2
10 % 2 == 0
2 % 0 == 2 --> b == 0 (True) 이 때 2가 최대 공약수이므로 2를 리턴 

10 * 12 == 120
120 // 2 == 60 (최소 공배수)
최소 공배수 = 두 수의 곱 // 최대 공약수

10 = [10, 20, 30, 40, 50, [60], 70, 80, ...]
12 = [12, 24, 36, 48, [60], 72, 84, 96, 108]
"""

import sys


def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a


for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))
 