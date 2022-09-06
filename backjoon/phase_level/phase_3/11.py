N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []

for i in range(N):
    if A[i] < X:
        B.append(str(A[i]))
print(' '.join(B))
print(B)
