
import sys
sys.setrecursionlimit(100000)

def factorial(a):
    if a == 1 or a == 0:
        return 1
    return a * factorial(a-1)


N, K = map(int, sys.stdin.readline().split())
BC = factorial(N) // (factorial(N - K) * factorial(K))

print(BC % 10007)
