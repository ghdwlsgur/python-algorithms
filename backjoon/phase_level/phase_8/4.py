
a, b = map(int, input().split())


cnt = 0
for i in range(a, b+1):
    if i > 1:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
            if cnt >= 1:
                break
        if cnt == 0:
            print(i)
        cnt = 0
