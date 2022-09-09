import sys

num = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for i in range(num)]
cnt = 0


def width():
    global cnt

    for i in range(num):
        c = 1
        for j in range(1, num):
            if arr[i][j] == arr[i][j-1]:
                c += 1
            else:
                if cnt < c:
                    cnt = c
                c = 1
        if cnt < c:
            cnt = c


def height():
    global cnt

    for i in range(num):
        c = 1
        for j in range(1, num):
            if arr[j][i] == arr[j-1][i]:
                c += 1
            else:
                if cnt < c:
                    cnt = c
                c = 1
        if cnt < c:
            cnt = c


for i in range(num):
    for j in range(1, num):
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        width()
        height()
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]

for i in range(num):
    for j in range(1, num):
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
        width()
        height()
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
print(cnt)
