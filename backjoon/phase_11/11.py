
import sys

tot, num = map(int, sys.stdin.readline().split())
print(sorted(list(map(int, sys.stdin.readline().split())),
      reverse=True)[num-1])
