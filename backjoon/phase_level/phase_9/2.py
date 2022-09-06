
n = int(input())
l = []
if n <= 20 or n == 0:
    for i in range(0, n+1):
        if i == 0:
            l.append(0)
        elif i == 1 or i == 2:
            l.append(1)
        else:
            l.append(l[i-1] + l[i-2])
print(l[n])
