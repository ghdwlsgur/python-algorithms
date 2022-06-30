import sys


def gcd(a, b):
    while(b):
        a, b = b, b % a
    return a


n = int(sys.stdin.readline().rstrip())

l = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    l.append(num)

if n == 2:
    if max(l[0], l[1]) % min(l[0], l[1]) == 0:
        print(min(l[0], l[1]))
else:
    gcd_l = []
    for i in range(0, n):
        for j in range(i+1, n):
            gcd_l.append(gcd(l[i], l[j]))

    gcd_l = list(set(gcd_l))
    print(gcd_l)

    for i in gcd_l:
        cnt = 0
        if i != 1:
            for j in range(0, n):
                if l[0] % i == l[j] % i:
                    cnt += 1
            if cnt == n:
                print(i, end=" ")
