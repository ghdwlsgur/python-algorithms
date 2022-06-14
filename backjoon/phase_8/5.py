
# 1
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0
#     res = 0
#     for i in range(n+1, n*2+1):
#         if i == 1:
#             break
#         else:
#             for j in range(2, int(i**0.5)+1):
#                 if i % j == 0:
#                     cnt += 1
#                     break
#             if cnt == 0:
#                 res += 1
#             cnt = 0
#     print(res)
#     res = 0

# 2
# def is_not_decimal(i):
#     if i == 1:
#         return False
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             return False
#     return True
# while True:
#     n = int(input())

#     cnt = 0
#     if n == 0:
#         break
#     else:
#         for i in range(n+1, n*2+1):
#             if is_not_decimal(i):
#                 cnt += 1
#         print(cnt)

# 3
def is_not_decimal(i):
    if i == 1:
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True


arange = list(range(2, 246912))
l = []
for i in arange:
    if is_not_decimal(i):
        l.append(i)
while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in l:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
