
# 전국대회 선발고사
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    print(arr)
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]


rank = [1, 2, 3]
attendance = [True, True, True]
print(solution(rank, attendance))