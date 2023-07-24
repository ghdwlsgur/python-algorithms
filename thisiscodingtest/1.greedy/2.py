
# n, m, k = map(int, input().split())
#
# l = list(map(int, input().split()))
#
# answer = []
# # 카운트 변수 초기화
# cnt = 0
# for i in range(m):
#     # 최댓값 저장
#     max_num = max(l)
#     # 카운트가 k번 만큼 순회할 때, 가장 큰 수를 리스트에서 임시 삭제 후
#     # 두 번째로 큰 수를 answer 리스트에 추가
#     # 다시 가장 큰 수를 리스트에 추가하여 다음 카운트에 사용
#     if cnt == k:
#         l.remove(max_num)
#         answer.append(max(l))
#         l.append(max_num)
#         # 카운트 초기화
#         cnt = 0
#     else:
#         # 가장 큰 수 추가
#         answer.append(max_num)
#         cnt += 1
#
# print(sum(answer))


# N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort() # 입력받은 수들 정렬하기
#
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두 번쨰로 큰 수
#
# result = 0
#
# while True:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result += second # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기
#
# print(result)


n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)