from collections import deque

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs(idx):
    global visited
    q = deque([idx])
    visited[idx] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)