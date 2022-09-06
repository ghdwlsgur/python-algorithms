num = int(input())

a = list(map(int, input().split()))


max = 1
for i in a:
    if max < i:
        max = i

sum = 0
for i in a:
    i = i / max * 100
    sum = sum + i

print(sum / num)
