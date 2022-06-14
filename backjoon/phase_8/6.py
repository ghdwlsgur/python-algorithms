
def is_decimal(i):
    if i == 1:
        return False
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            return False
    return True


for i in range(int(input())):
    n = int(input())

    a = n // 2
    b = n - (n // 2)
    if is_decimal(a) and a == b:
        print(a, a)
    else:
        i = 1
        while True:
            a -= i
            b = n - a
            if is_decimal(a) and is_decimal(b):
                break
        print(a, b)
