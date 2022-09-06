
import sys
sys.setrecursionlimit(100000)


def factorial(a):
    if a == 1 or a == 0:
        return 1
    return a * factorial(a-1)


for _ in range(int(sys.stdin.readline().rstrip())):
    N, K = map(int, sys.stdin.readline().split())
    print(int(factorial(K) / (factorial(K-N) * factorial(N))))
