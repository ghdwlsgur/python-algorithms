import sys
on_off = True
while on_off:
    a, b, c = map(int, sys.stdin.readline().split())
    if a + b + c == 0:
        on_off = False
    else:
        max_n = max(a, b, c)
        min_n = min(a, b, c)
        n = (a + b + c) - max_n - min_n
        if max_n ** 2 == (min_n ** 2) + (n ** 2):
            print("right")
        else:
            print("wrong")
