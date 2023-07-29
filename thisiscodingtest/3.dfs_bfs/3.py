from collections import deque

def dfs(idx):
    global visited
    # 현재 노드 방문 처리
    visited[idx] = True
    print(idx, end=' ')
    print(visited)
    # 1부터 N까지 반복
    for next in range(1, N+1):
        # next번 노드를 방문하지 않았으면서 next번 노드와 연결되었을 때 (인접 노드일 때)
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs(idx):
    global visited
    q = deque([idx])
    # 현재 노드 방문 처리
    visited[idx] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for next in range(1, N+1):
            # next번 노드를 방문하지 않았으면서 next번 노드와 연결되었을 때 (인접 노드일 때)
            if not visited[next] and graph[cur][next]:
                # 방문 처리
                visited[next] = True
                q.append(next)


# N, M, V(시작점)를 시용자로부터 입력
N, M, V = map(int, input().split())

# 인덱스상 0부터 시작하므로 1추가
graph = [[False] * (N + 1) for _ in range(N + 1)]

# 그래프 초기화
for _ in range(M):
    a, b = map(int, input().split())
    # 두 노드가 이어질 경우 각 노드의 기준으로 True
    # 예를 들어, 1번 노드와 2번 노드가 연결될 때, graph[1][2]외 graph[2][1] 모두 True
    graph[a][b] = True
    graph[b][a] = True

# 방문 리스트 생성
visited = [False] * (N + 1)
dfs(V) # DFS 실행
print()

# 방문 리스트 초기화
visited = [False] * (N + 1)
bfs(V) # BFS 실행
