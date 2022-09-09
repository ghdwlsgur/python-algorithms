import sys

arr = [0 for _ in range(9)]


for i in range(9):
    input = int(sys.stdin.readline().rstrip())
    arr[i] = input

target = sum(arr)
while target > 100:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if target - arr[i] - arr[j] == 100:
                    arr[i], arr[j] = 0, 0
                    target = 100
                    break
[print(i) for i in sorted(arr) if i != 0]
