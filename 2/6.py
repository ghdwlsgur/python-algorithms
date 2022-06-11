time = input().split()
hh = int(time[0])
mm = int(time[1])

add = int(input())
total = hh * 60 + mm + add


if total // 60 >= 24:
    hh = total // 60 % 24
    print(hh, total % 60)
else:
    print(total // 60, total % 60)
