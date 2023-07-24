
# 나의 풀이
# n, m = map(int, input().split())
#
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
#
# answer = []
# for v in l:
#     v.sort()
#     answer.append(v[0])
#
# print(max(answer))

# 동빈나 풀이
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result)


n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)