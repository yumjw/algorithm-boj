from collections import deque

N = int(input())
Lines = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(Lines):
    node_1, node_2 = list(map(int, (input().split())))
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

def bfs(graph, start_node, visited):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited

result = bfs(graph, 1, visited)
print(sum(result)-1)