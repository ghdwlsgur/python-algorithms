
num = int(input())

for i in range(0, num):
    n = list(map(int, input().split()))
    sum = n[0] + n[1]
    print("Case #%d: %d + %d = %d" % (i + 1, n[0], n[1], sum))
