from collections import deque
import sys

global queue
queue = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    input = sys.stdin.readline().split()

    if input[0] == "push":
        queue.appendleft(int(input[1]))
    if input[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print("-1")
    if input[0] == "front":
        print(queue[-1] if queue else "-1")
    if input[0] == "back":
        print(queue[0] if queue else "-1")
    if input[0] == "size":
        print(len(queue))
    if input[0] == "empty":
        print("0" if queue else "1")
