import sys

stack = []
for _ in range(int(sys.stdin.readline().rstrip())):
    input = int(sys.stdin.readline().rstrip())

    if input == 0:
        stack.pop()
    else:
        stack.append(input)

print(sum(stack))
