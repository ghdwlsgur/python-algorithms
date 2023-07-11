

n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0

for k in range(1, n+1):
    result += sum(p[0:k])

print(result)
