

h, b, c, s = map(float, input().split())

print("%.1f MB" % (h * b * c * s/8/1024/1024))
