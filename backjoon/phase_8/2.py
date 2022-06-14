a = int(input())
b = int(input())

l = []
cnt = 0
for i in range(a, b+1):
    if i > 1:
        for j in range(2, i):
            if i != j and i % j == 0:
                cnt += 1
            if cnt >= 1:
                break
        if cnt == 0:
            l.append(i)
        cnt = 0


min = b
total = 0
if len(l) != 0:
    for i in l:
        if min > i:
            min = i
        total += i
    print("%d\n%d" % (total, min))
else:
    print("-1")
