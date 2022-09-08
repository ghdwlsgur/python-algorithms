import sys


open = "("
close = ")"
for _ in range(int(sys.stdin.readline().rstrip())):
    input = list(sys.stdin.readline().rstrip())
    tot = 0
    for bracket in input:
        if bracket == open:
            tot += 1
        elif bracket == close:
            tot -= 1

        if tot < 0:
            break
    print("YES" if tot == 0 else "NO")
