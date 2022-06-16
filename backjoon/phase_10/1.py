
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# l = len(num)
# ans = 0
# for i in range(0, l-2):
#     for j in range(i+1, l-1):
#         for k in range(j+1, l):
#             print("[", num[i], num[j], num[k], "]")
#             if(num[i] + num[j] + num[k] > m):
#                 continue
#             else:
#                 ans = max(ans, num[i] + num[j] + num[k])
# print(ans)

# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# l = len(num)
# ans = 0
# for i in range(0, l-2):
#     for j in range(i+1, l-1):
#         for k in range(j+1, l):
#             if num[i] + num[j] + num[k] > m:
#                 continue
#             else:
#                 ans = max(ans, num[i] + num[j] + num[k])
# print(ans)

# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# l = len(num)
# ans = 0
# for i in range(0, l-2):
#     for j in range(i+1, l-1):
#         for k in range(j+1, l):
#             if num[i] + num[j] + num[k] > m:
#                 continue
#             else:
#                 ans = max(ans, num[i] + num[j] + num[k])
# print(ans)

n, m = map(int, input().split())
num = list(map(int, input().split()))
l = len(num)
res = 0

for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if num[i] + num[j] + num[k] > m:
                continue
            else:
                res = max(res, num[i] + num[j] + num[k])

print(res)


""" 
[5, 6, 7], [5, 6, 8], [5, 6, 9]
[5, 7, 8], [5, 7, 9]
[5, 8, 9]
[6, 7, 8], [6, 7, 9]
[6, 8, 9]
[7, 8, 9]
"""
