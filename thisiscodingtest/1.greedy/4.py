
# 나의 풀이
# n, k = map(int, input().split())
#
# cnt = 0
#
# # n이 1이 될 때까지 계속 수행
# while n != 1:
#     # 실행 횟수 1 증가
#     cnt += 1
#     # n이 k로 나누어 떨어진다면 나누기
#     if n % k == 0:
#         n = n // k
#     # 나누어 떨어지지 않는다면 1차감
#     else:
#         n -= 1
#
#
# print(cnt)

# 동빈나 풀이1
# n, k = map(int, input().split())
# result = 0
#
# # n이 k 이상이라면 k로 계속 나누기
# while n >= k:
#     # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)

# 동빈나 풀이2
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)


