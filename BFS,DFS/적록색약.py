import sys
sys.setrecursionlimit(1000000)

N = int(input())

graph = []
for _ in range(N):
    row = list(sys.stdin.readline().rstrip())
    graph.append(row)

nodes = [[y, x] for y in range(N) for x in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

general_count = 0
visited = [([False]*N) for _ in range(N)]
def dfs(start_node):
    y, x = start_node
    visited[y][x] = True
    node_color = graph[y][x]

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if 0 <= new_y < N and 0 <= new_x < N:
            if not visited[new_y][new_x] and graph[new_y][new_x] == node_color:
                dfs([new_y, new_x])

for node in nodes:
    y, x = node
    if not visited[y][x]:
        dfs(node)
        general_count += 1


for y, row in enumerate(graph):
    for x, element in enumerate(row):
        if graph[y][x] == 'G':
            graph[y][x] = 'R'


special_count = 0
visited = [([False]*N) for _ in range(N)]

for node in nodes:
    y, x = node
    if not visited[y][x]:
        dfs(node)
        special_count += 1

print(f'{general_count} {special_count}')