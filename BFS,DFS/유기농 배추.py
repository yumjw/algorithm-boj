# T = int(input())
M, N, K = map(int, input().split())

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

count = 0
stack = []
coordinate_list = []
graph = [([0]*M) for i in range(N)] # NxM 모양 배추밭


for i in range(K):
    check_x, check_y = map(int, input().split())
    graph[check_y][check_x] = 1
    coordinate_list.append((check_x, check_y))

print(graph)

for coordinate in coordinate_list:
    x = coordinate[0]
    y = coordinate[1]

    if graph[y][x] == 1:

        stack.append((x, y))
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < N) and (0 <= ny < M):
                    print(nx, ny)
                    if graph[ny][nx] == 1:
                        stack.append((nx, ny))
            graph[y][x] = 0
        count += 1

print(count)