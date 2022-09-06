import sys
from itertools import product


# N, M = map(int, sys.stdin.readline().split())

# cache = []
# for i in range(1, N+1):
#     if M == 1:
#         print(i)
#     else:
#         cache.append(i)

# for i in product(cache, repeat=M):
#     print(*i)


N, M = [int(x) for x in sys.stdin.readline().split()]
answer = []


def route(N, M):
    for i in range(1, N+1):
        answer.append(str(i))
        if len(answer) >= M:
            print(" ".join(answer))
        else:
            route(N, M)
        answer.pop()


route(N, M)
