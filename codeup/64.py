
a, b, c = map(int, input().split())


print((a if a < b else b) if ((b if b < a else a) < c) else c)
