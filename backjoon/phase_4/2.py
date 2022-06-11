

arr = []
max = 1
idx = 0
for i in range(0, 9):
    n = int(input())
    arr.append(n)
    if max < arr[i]:
        max = arr[i]
        idx = i + 1
print(max)
print(idx)
