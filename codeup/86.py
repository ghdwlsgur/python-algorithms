
n = int(input())


sum = 0
for i in range(0, n+1):
    sum += i
    if n <= sum:
        print(sum)
        break
