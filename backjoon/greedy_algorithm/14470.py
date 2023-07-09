
temp = int(input())
want = int(input())
c = int(input())
d = int(input())
e = int(input())

tot = 0
if temp < 0:
    tot += abs(temp) * c
    tot += d
    dis = want - 0
else:
    dis = want - temp
tot += dis * e
print(tot)
