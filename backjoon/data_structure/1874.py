import sys

stack = []
output = []
flag = True
cur = 1


for i in range(int(sys.stdin.readline().rstrip())):
    input = int(sys.stdin.readline().rstrip())

    while cur <= input:
        stack.append(cur)
        output.append("+")
        cur += 1

    if stack[-1] == input:
        stack.pop()
        output.append("-")
    else:
        print("NO")
        flag = False
        break

if flag:
    [print(i) for i in output]
