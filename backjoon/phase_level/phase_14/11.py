import sys
n = int(sys.stdin.readline().rstrip())


def factorial(a):
    if a == 1 or a == 0:
        return 1
    return a * factorial(a-1)


cnt = 0
l = " ".join(str(factorial(n))).split(" ")
for i in range(len(l)-1, -1, -1):
    if i == len(l)-1 and l[i] == '0':
        cnt += 1
    else:
        if l[i] == '0' and l[i+1] == '0':
            cnt += 1
        else:
            break

print(cnt)
