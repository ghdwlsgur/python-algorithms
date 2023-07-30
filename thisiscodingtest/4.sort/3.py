

n, k = map(int, input().split())

l = []
for i in range(2):
    l.append(list(map(int, input().split())))

A = sorted(l[0])
B = sorted(l[1], reverse=True)

for i in range(k):
    A[i], B[i] = B[i], A[i]

print(sum(A))


