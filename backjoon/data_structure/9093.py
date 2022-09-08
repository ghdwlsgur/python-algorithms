import sys

for i in range(int(sys.stdin.readline().rstrip())):
    input = list(sys.stdin.readline().split())
    for word in input:
        print(word[::-1], end=" ")
    print("")
