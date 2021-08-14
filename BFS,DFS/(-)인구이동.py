from collections import deque
import math

N, L, R = map(int, input().split())

graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [([False] * N) for _ in range(N)]
countries = [[r, c] for r in range(N) for c in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

current_day = 1
keep_going = True

while True:

    keep_going = False
    for country in countries:
        r, c = country
        print(visited)

        if visited[r][c]+1 == current_day:

            queue = deque()
            united = []
            people = 0

            queue.append((r,c))
            united.append((r,c))
            people += graph[r][c]
            visited[r][c] = True

            while queue:
                current_r, current_c = queue.popleft()

                for i in range(4):
                    new_r = current_r + dr[i]
                    new_c = current_c + dc[i]

                    if 0 <= new_r < N and 0 <= new_c < N:
                        if visited[new_r][new_c]+1 == current_day and (L <= abs(graph[r][c] - graph[new_r][new_c]) <= R):
                            keep_going = True
                            queue.append((new_r, new_c))
                            united.append((new_r, new_c))
                            people += graph[new_r][new_c]
                            visited[new_r][new_c] = True

            united_number = math.floor(people / len(united))
            for country_united in united:
                temp_r, temp_c = country_united
                graph[temp_r][temp_c] = united_number

    if not keep_going:
        break
    else:
        current_day += 1

print(current_day)