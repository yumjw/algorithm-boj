T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(T):
    M, N, K = map(int, input().split())

    count = 0
    stack = []
    coordinate_list = []
    graph = [([0]*M) for i in range(N)] # NxM 모양 배추밭

    for i in range(K):
        check_x, check_y = map(int, input().split())
        graph[check_y][check_x] = 1
        coordinate_list.append((check_x, check_y))

    for coordinate in coordinate_list:
        x = coordinate[0]
        y = coordinate[1]

        if graph[y][x] == 1:
            stack.append((x, y))
            while stack:
                x, y = stack.pop()
                graph[y][x] = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (0 <= nx <= M-1) and (0 <= ny <= N-1):
                        if graph[ny][nx] == 1:
                            stack.append((nx, ny))
            count += 1

    print(count)