from collections import deque

M, N = map(int, input().split())

graph = []
visited = [([False]*M) for _ in range(N)]
tomato_riped = deque()
count=0
able=True

max_result_list = []

for i in range(N):

    tomato_row = list(map(int, input().split()))

    for idx, element in enumerate(tomato_row):
        if element == 1:
            tomato_riped.append((i, idx))

    graph.append(tomato_row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while tomato_riped:
    y, x = tomato_riped.popleft()
    visited[y][x] = True

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if (0 <= new_y < N) and (0 <= new_x < M):
            if graph[new_y][new_x] == 0 and visited[new_y][new_x] == False:
                tomato_riped.append((new_y, new_x))
                graph[new_y][new_x] = graph[y][x] + 1
                visited[new_y][new_x] == True

for i in range(N):
    if 0 in graph[i] :
        able=False
    max_result_list.append(max(graph[i]))

if able:
    print(max(max_result_list)-1)
else:
    print(-1)