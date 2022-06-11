time = input().split()
hh = int(time[0])
mm = int(time[1])

total = hh * 60 + mm
if total >= 45:
    total = total - 45
    print(total // 60, total % 60)
else:
    hh = 23
    print(hh, mm + 15)
