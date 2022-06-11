num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])


if a == b and b == c and a == c:
    print(10000 + (a * 1000))
elif a == b or b == c:
    print(1000+b*100)
elif a == c:
    print(1000 + c * 100)
else:
    if (a > b) and (a > c):
        print(a * 100)
    elif b > a and b > c:
        print(b * 100)
    else:
        print(c * 100)
