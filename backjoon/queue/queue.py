import sys

global queue
queue = []


def push(n):
    queue.append(n)


def pop():
    global queue
    if len(queue) > 0:
        print(queue[0:1][0])
        queue = list(queue[1:])
    else:
        print("-1")


for i in range(int(sys.stdin.readline().rstrip())):
    input = sys.stdin.readline().split()

    if input[0] == "push":
        push(int(input[1]))
    if input[0] == "pop":
        pop()
    if input[0] == "front":
        print(queue[0:1][0] if len(queue) > 0 else "-1")
    if input[0] == "back":
        print(queue[-1:][0] if len(queue) > 0 else "-1")
    if input[0] == "empty":
        print("0" if len(queue) > 0 else "1")
    if input[0] == "size":
        print(len(queue))
