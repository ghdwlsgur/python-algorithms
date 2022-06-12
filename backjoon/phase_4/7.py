# num = int(input())

# sum = 0
# cnt = 0
# result = []
# for i in range(0, num):
#     n = list(map(int, input().split()))

#     for k in n:
#         sum = sum + k

#     sum = sum - n[0]

#     for k in n:
#         if k > (sum / n[0]):
#             cnt = cnt + 1

#     result.append((cnt / n[0]) * 100)
#     sum = 0
#     cnt = 0

# for res in result:
#     output = round(res, 3)
#     format_str = format(output, ".3f")
#     print(format_str+'%')

for i in range(int(input())):
    a = list(map(int, input().split()))
    b = 0
    for j in range(1, len(a)):
        if a[j] > sum(a[1:]) / a[0]:
            b += 1
        else:
            pass
    print(format(b/a[0] * 100, '.3f'), '%', sep="")
