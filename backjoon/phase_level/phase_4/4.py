
result = []
cnt = 0
for i in range(0, 10):
    n = int(input())
    result.append(n % 42)

for i in set(result):
    cnt = cnt + 1

print(cnt)
