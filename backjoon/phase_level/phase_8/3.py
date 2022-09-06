# 72 // 2 = 36
# 36 // 2 = 18
# 18 // 2 = 9
# 9 // 3 = 3
# 3 // 3 = 1

n = int(input())

i = 2
while n > 1:
    if n % i == 0:
        n //= i
        print(i)
        i = 2
    else:
        i += 1
