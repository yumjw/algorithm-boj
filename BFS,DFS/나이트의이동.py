from collections import deque

T = int(input())
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, -2, 2, -2, 2]


for i in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    visited = [([0]*I) for _ in range(I)]
    queue = deque()

    queue.append([start_x, start_y])
    arrived = False

    while queue:
        x, y = queue.popleft()

        if dest_x == x and dest_y == y:
            answer = 0
            break

        for i in range(8):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if (0 <= new_x < I) and (0 <= new_y < I):

                if new_x == dest_x and new_y == dest_y:
                    arrived = True
                    answer = visited[y][x] + 1
                    break

                if visited[new_y][new_x] == 0:
                    queue.append([new_x, new_y])
                    visited[new_y][new_x] = visited[y][x] + 1
        if arrived:
            break

    print(answer)