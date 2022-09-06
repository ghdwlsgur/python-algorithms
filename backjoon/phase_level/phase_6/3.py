

words = input()
res = []

for i in range(0, 26):
    res.append(-1)

i = 0
for alpha in words:
    if res[ord(alpha) - 97] == -1:
        res[ord(alpha) - 97] = i
    i += 1

for out in res:
    print(out, end=" ")
