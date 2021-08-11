import sys
sys.setrecursionlimit(1000000)

N = int(input())

graph = []
for _ in range(N):
    row = list(sys.stdin.readline().rstrip())
    graph.append(row)

visited = [([False]*N) for _ in range(N)]
nodes = [[y, x] for y in range(N) for x in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
count = 0

def dfs_general(start_node):
    y, x = start_node
    visited[y][x] = True
    node_color = graph[y][x]

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if 0 <= new_y < N and 0 <= new_x < N:
            if not visited[new_y][new_x] and graph[new_y][new_x] == node_color:
                dfs_general([new_y, new_x])

for node in nodes:
    y, x = node
    if not visited[y][x]:
        dfs_general(node)
        count += 1

print(count)