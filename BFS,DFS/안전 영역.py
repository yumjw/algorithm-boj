import sys
sys.setrecursionlimit(1000000)

N = int(input())
max_rain = 0
max_count = 0
graph = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    if max(row) > max_rain:
        max_rain = max(row)
    graph.append(row)

nodes = [(y, x) for y in range(N) for x in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(start_node, rain):
    y, x = start_node
    visited[y][x] = True

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if 0 <= new_y < N and 0 <= new_x < N:
            if not visited[new_y][new_x] and graph[new_y][new_x] > rain:
                dfs([new_y, new_x], rain)

for rain in range(max_rain):
    visited = [([False] * N) for _ in range(N)]
    count = 0

    for node in nodes:
        y, x = node
        if not visited[y][x] and graph[y][x] > rain:
            dfs([y, x], rain)
            count += 1
    if max_count < count:
        max_count = count

print(max_count)