
a = int(input())
n = list(map(int, input().split()))

res = len(n)
for i in n:
    if i > 1:
        for j in range(2, i):
            if i != j and i % j == 0:
                res -= 1
                break
    else:
        res -= 1
print(res)
