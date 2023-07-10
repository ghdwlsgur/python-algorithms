

i = 0
while True:
    i += 1
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    if c % b < a:
        d = c % b
    else:
        d = a
    print("Case %d: %d" % (i, ((c // b) * a) + d))
