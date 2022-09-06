
import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

all = set(a).union(set(b))
print(len(list(all.difference(set(b)))) + len(all.difference(set(a))))
