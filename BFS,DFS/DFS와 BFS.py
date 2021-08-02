from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

dfs_result = []
bfs_result = []

queue = deque()
stack = []

for i in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph:
    node.sort()


# dfs - Stack version
visited = [False]*(N+1)

stack.append(V)
visited[V] = True
dfs_result.append(V)

while stack:
    current_node = stack.pop()
    adj_nodes = graph[current_node]
    for i in adj_nodes:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs_result.append(i)
            break

## dfs - Recursive fn version
# visited = [False]*(N+1)

# def dfs(v, graph, visited):
#     visited[v] = True
#     dfs_result.append(v)
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, graph, visited)
#
# dfs(V, graph, visited)
print(' '.join(list(map(str, dfs_result))))


# bfs
visited = [False]*(N+1)

visited[V] = True
queue.append(V)
bfs_result.append(V)

while queue:
    current_node = queue.popleft()
    adj_nodes = graph[current_node]

    for i in adj_nodes:
        if not visited[i]:
            visited[i] = True
            bfs_result.append(i)
            queue.append(i)
print(' '.join(list(map(str, bfs_result))))