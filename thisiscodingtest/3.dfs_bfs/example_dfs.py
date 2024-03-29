def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def dfs2(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs2(graph, i, visited)

def dfs3(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs3(graph, i, visited)

def dfs4(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs4(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8], # 1번 노드와 연결된 노드 (2, 3, 8)
    [1, 7], # 2번 노드와 연결된 노드 (1, 7)
    [1, 4, 5], # 3번 노드와 연결된 노드 (1, 4, 5)
    [3, 5], # 4번 노드와 연결된 노드 (3, 5)
    [3, 4], # 5번 노드와 연결된 노드 (3, 4)
    [7], # 6번 노드와 연결된 노드 (7)
    [2, 6, 8], # 7번 노드와 연결된 노드 (2, 6, 8)
    [1, 7] # 8번 노드와 연결된 노드 (1, 7)
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
print(dfs(graph, 1, visited))

