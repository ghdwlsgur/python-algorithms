

a, b, c = map(int, input().split())


if b >= c:
    print(-1)
else:
    print(int(a / (c-b)) + 1)

#  1   1     1     1
# 2 3 3 4 4 4 5 5 5 6 6 6 6 6
