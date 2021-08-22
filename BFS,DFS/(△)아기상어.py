# https://www.acmicpc.net/problem/16236
# 70%에서 오류
from collections import deque

N = int(input())
graph = []

for _ in range(N):
    row = list(map(int, input().split()))

    for idx, value in enumerate(row):
        if value == 9:
            start_node = [_, idx]
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

second = 0
baby_size = 2
sizeup_count = baby_size


while True:
    visited = [([False] * N) for _ in range(N)]
    visited[start_node[0]][start_node[1]] = True

    queue = deque()
    queue.append(start_node)
    min_distance = 100
    min_distance_list = []
    distance_matrix = [([0] * N) for _ in range(N)]

    while queue:
        current_y, current_x = queue.popleft()

        for i in range(4):
            new_y = current_y + dy[i]
            new_x = current_x + dx[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_y][new_x] and 0 <= graph[new_y][new_x] <= baby_size:

                    visited[new_y][new_x] = True
                    queue.append([new_y, new_x])
                    distance_matrix[new_y][new_x] = distance_matrix[current_y][current_x] + 1

                    if 0 < graph[new_y][new_x] < baby_size:
                        distance = distance_matrix[new_y][new_x]

                        if min_distance > distance:
                            min_distance = distance
                            min_distance_list = [[new_y, new_x]]
                        elif min_distance == distance:
                            min_distance_list.append([new_y, new_x])


    if len(min_distance_list) == 0:
        print(second)
        break

    else:
        sizeup_count -= 1
        if sizeup_count == 0:
            baby_size += 1
            sizeup_count = baby_size
        second += min_distance
        graph[start_node[0]][start_node[1]] = 0
        start_node = min(min_distance_list)
        print(start_node)
        graph[start_node[0]][start_node[1]] = 9