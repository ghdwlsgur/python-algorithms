

num = input().split()

second = 0
for i in "".join(num):
    if ord(i) >= 65 and ord(i) <= 67:
        second += 3
    elif ord(i) >= 68 and ord(i) <= 70:
        second += 4
    elif ord(i) >= 71 and ord(i) <= 73:
        second += 5
    elif ord(i) >= 74 and ord(i) <= 76:
        second += 6
    elif ord(i) >= 77 and ord(i) <= 79:
        second += 7
    elif ord(i) >= 80 and ord(i) <= 83:
        second += 8
    elif ord(i) >= 84 and ord(i) <= 86:
        second += 9
    else:
        second += 10
print(second)
