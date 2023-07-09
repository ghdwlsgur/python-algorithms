
a, b, c, d = map(int, input().split())

if d == 1:
    print(a)
else:
    num = a * b + c
    for i in range(1, d-1):
        num = num * b + c
    print(num)
