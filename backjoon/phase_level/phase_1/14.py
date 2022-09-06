
import sys

arr = [1, 1, 2, 2, 2, 8]
num = sys.stdin.readline().split()
[print(int(arr[i]) - int(num[i]), end=" ") for i in range(0, 6)]
