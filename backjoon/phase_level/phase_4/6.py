
sum = 0
cnt = 0
for i in range(int(input())):
    a = input()
    for j in a:
        if j == 'O':
            cnt = cnt + 1
            sum = sum + cnt
        else:
            cnt = 0
            pass
    print(sum)
    sum = 0
    cnt = 0
