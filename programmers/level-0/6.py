# def solution(n):
#     answer = [[0 for _ in range(n)] for _ in range(n)]
#
#     now = [0, 0]
#     direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     k = 1
#     idx = 0
#     while k <= n ** 2:
#         answer[now[0]][now[1]] = k
#         next_x, next_y = now[0] + direction[idx][0], now[1] + direction[idx][1]
#
#         if next_x >= n or next_y >= n or next_x < 0 or next_y < 0 or answer[next_x][next_y] != 0:
#             idx = (idx + 1) % 4
#
#         now[0] += direction[idx][0]
#         now[1] += direction[idx][1]
#         k += 1
#
#     return answer
# 정수를 나선형으로 배치하기

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    now = [0, 0]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    k = 1
    idx = 0

    while k <= n ** 2:
        answer[now[0]][now[1]] = k

        next_x, next_y = now[0] + direction[idx][0], now[1] + direction[idx][1]

        if next_x >= n or next_y >= n or next_x < 0 or next_y < 0 or answer[next_x][next_y] != 0:
            idx = (idx + 1) % 4

        now[0] += direction[idx][0]
        now[1] += direction[idx][1]
        k += 1

    return answer

print(solution(4))
print(solution(5))
