a = int(input())
b = int(input())
c = int(input())
tot = a * b * c
arr = ''.join(str(tot))


output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in arr:
    for j in range(0, 10):
        if int(i) == j:
            output[j] = output[j] + 1

for out in output:
    print(out)
