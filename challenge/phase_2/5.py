
time = input().split()

hh = int(time[0])
mm = int(time[1])

alert = (hh * 60 + mm)
if alert > 45:
    alert = alert - 45
    print(alert//60, alert % 60)
else:
    hh = 23
    print(hh, mm + 15)
