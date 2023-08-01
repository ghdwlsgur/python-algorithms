

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

a, b = l[0], l[-1]

result = []
for i in range(a, b+1):
    sum = 0
    for k in l:
        if k > i:
            sum += k - i
    if sum == m:
        result.append(i)

print(max(result))



# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# l.sort()
#
# low, high = 0, max(l)
#
# result = 0
#
# while low <= high:
#     mid = (low + high) // 2
#     total = 0
#     for i in l:
#         if i > mid:
#             total += i - mid
#     if total < m:
#         high = mid - 1
#     else:
#         result = mid
#         low = mid + 1
#
# print(result)

