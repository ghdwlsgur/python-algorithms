
n = int(input())

change = 1000 - n
coin_n = 0
while change != 0:
    if change // 500 >= 1:
        coin_n += change // 500
        change %= 500
    elif change // 100 >= 1:
        coin_n += change // 100
        change %= 100
    elif change // 50 >= 1:
        coin_n += change // 50
        change %= 50
    elif change // 10 >= 1:
        coin_n += change // 10
        change %= 10
    elif change // 5 >= 1:
        coin_n += change // 5
        change %= 5
    elif change < 5:
        coin_n += change
        change = 0

print(coin_n)
