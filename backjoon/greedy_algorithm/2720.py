
# 쿼터($0.25), 다임($0.1), 니켈($0.05), 페니($0.01)

for i in range(0, int(input())):
    money = int(input())
    q = money % 25
    d = q % 10
    n = d % 5
    print(money // 25, q // 10, d // 5, n // 1)
