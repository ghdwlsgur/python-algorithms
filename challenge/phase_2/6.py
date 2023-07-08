num = input().split()
hh = int(num[0])
mm = int(num[1])
after = int(input())

tot = (hh * 60 + mm) + after
if tot//60 >= 24:
    print(tot//60-24, tot % 60)
else:
    print(tot//60, tot % 60)
