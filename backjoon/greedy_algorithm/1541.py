

n = input().split('-')

answer = 0

x = sum(map(int, (n[0].split('+'))))


if n[0] == '-':
    answer -= x
else:
    answer += x


for x in n[1:]:
    x = sum(map(int, x.split("+")))
    answer -= x
print(answer)
