from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
maze_graph = []
queue = deque()

for i in range(N):
    row = list(map(int, list(input())))
    maze_graph.append(row)

visited = [([0]*M) for _ in range(N)]

coordinates_list = [[x,y] for x in range(N) for y in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 1
queue.append([0,0])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x==(N-1) and y==(M-1):
        break

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if (0 <= new_x < N) and (0 <= new_y < M):
            if visited[new_x][new_y] == 0 and maze_graph[new_x][new_y] == 1:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append([new_x, new_y])

print(visited[N-1][M-1])