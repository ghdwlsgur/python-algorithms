start = int(input())

cnt = 0
init = start
while True:
    start = (start % 10) * 10 + ((start // 10) + (start % 10)) % 10
    cnt = cnt + 1
    if init == start:
        break
print(cnt)
