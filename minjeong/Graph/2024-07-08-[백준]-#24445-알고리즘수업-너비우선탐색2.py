import sys
from collections import deque

input = sys.stdin.readline

# BFS 함수
def bfs(v, graph, visited):
    queue = deque([v])
    order = 1
    while queue: # 큐가 빌 때까지 반복
        # 큐에서 원소를 하나 뽑아 node에 대입한다.
        node = queue.popleft()
        if visited[node] == 0:
            visited[node] = order  # 방문하면 순서 넣기
            order += 1
            graph[node].sort(reverse=True) # 내림차순으로 인접노드 방문하기 위해 정렬
            for u in graph[node]:
                if visited[u] == 0: # 인접 노드 중에서 방문 안 한 노드면 bfs 탐색
                    queue.append(u)

# 초기화
n, m, r = map(int, input().strip().split()) # n: 정점의 수, m: 간선의 수, r: 시작 정점
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

# 그래프 연결
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r, graph, visited)

# 해당노드를 몇 번째로 방문했는지 출력
for i in range(1, len(visited)):
    print(visited[i])