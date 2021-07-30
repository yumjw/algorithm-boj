from collections import deque

N = int(input())
apartments = []

for i in range(N):
    ith_row_apartment = list(map(int, list(input())))
    apartments.append(ith_row_apartment)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
apartments_complex = []

visited = [([False] * N) for n in range(N)]
coordinates_list = [(x, y) for x in range(N) for y in range(N)]

for coordinate in coordinates_list:
    x, y = coordinate
    if (apartments[x][y] == 1) and (visited[x][y] == False):
        count = 1
        queue.append(coordinate)
        visited[x][y] = True
        while queue:
            current_x, current_y = queue.popleft()
            for i in range(4):
                next_x = current_x + dx[i]
                next_y = current_y + dy[i]

                if (0 <= next_x < N) and (0 <= next_y < N):
                    if (visited[next_x][next_y] == False) and (apartments[next_x][next_y] == 1):
                        next_coordinate = (next_x, next_y)
                        visited[next_x][next_y] = True
                        count += 1
                        queue.append(next_coordinate)

        apartments_complex.append(count)

print(apartments_complex)
