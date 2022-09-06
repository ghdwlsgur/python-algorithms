import sys

# l = [1, 2, 3]
# print(l[-1:])  # 3
# print(l[:-1])  # 1, 2
# l = list(l[:-1])
# print(len(l))
# print(l)


global stack

stack = []
for i in range(int(sys.stdin.readline().rstrip())):

    input = sys.stdin.readline().split()

    if input[0] == "push":
        stack.append(int(input[1]))
    if input[0] == "pop":
        if len(stack) > 0:
            print(stack[-1:][0])
            stack = list(stack[:-1])
        else:
            print("-1")
    if input[0] == "size":
        print(len(stack))
    if input[0] == "empty":
        if len(stack) > 0:
            print("0")
        else:
            print("1")
    if input[0] == "top":
        if len(stack) > 0:
            print(stack[-1:][0])
        else:
            print("-1")
