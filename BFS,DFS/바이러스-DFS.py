# DFS
N = int(input())
Lines = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(Lines):
    node_1, node_2 = list(map(int, (input().split())))
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

def dfs(graph, v, visited):
    visited[v] = True

    visited_list = []
    visited_list.append(v)

    for i in graph[v]:
        if not visited[i]:
            visited_list = visited_list + dfs(graph, i, visited)

    return visited_list

result = list(set(dfs(graph, 1, visited)))
print(len(result)-1)