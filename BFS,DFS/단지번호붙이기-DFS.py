import sys

N = int(sys.stdin.readline())

apartment_graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def dfs(graph, count, y, x):

    graph[y][x] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[ny][nx] == 1:
                count = dfs(graph, count + 1, ny, nx)


    return count


count_list = []
for i in range(N):
    for j in range(N):
        if apartment_graph[i][j] == 1:
            count_list.append(dfs(apartment_graph, 1, i, j))

print(len(count_list))
for cnt in sorted(count_list):
    print(cnt)
