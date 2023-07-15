import sys
import heapq

"""
현재 회의실에서의 회의가 끝나는 시간보다 다음 회의의 시작시간이 빠르면 
회의실을 하나 추가로 개설한다.

현재 회의실에서 회의가 끝나는 시간보다 다음 회의의 시작시간이 느리면 
현재 존재하는 회의실에서 이어서 회의 개최가 가능하다.
"""
n = int(sys.stdin.readline())

q = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))
