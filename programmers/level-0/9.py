# 안전지대

# 다른 사람 풀이
def solution(board):
    n = len(board)
    # 중복 제거를 위해 세트 자료형 사용
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            # 0일 경우 continue -> True
            if not x:
                continue
            # 1일 경우 최대 1칸 인접한 구역 danger 존에 인덱스 추가
            # 인덱스 범위는 이중 반복문으로 구현
            danger.update((i+di, j+dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])

    # 전체 구역에서 danger 구역의 합계를 차감
    # danger 존의 영역은 0이상 n미만으로 설정 (범위 설정)
    # 범위를 설정함으로써 전체 영역에 포함되지 않은 danger존 인덱스 포인트를 제거
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# 나의 풀이
# def solution(board):
#     position = []
#
#     check = 0
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 1:
#                 check += 1
#                 position.append((int(i), int(j)))
#
#     if check == len(board) * len(board[0]):
#         return 0
#
#     # i와 j는 -1부터 len(board)까지의 값을 가질 수 있음
#     for a, b in position:
#         for i in range(max(a-1, 0), min(a+2, len(board))):
#             for j in range(max(b-1, 0), min(b+2, len(board[0]))):
#                 board[i][j] = 1
#
#     cnt = 0
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 0:
#                 cnt += 1
#     return cnt



print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))