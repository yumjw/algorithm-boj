from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    node_1, node_2 = map(int, input().split())

    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

kv_list = []

for person in range(1, N+1):
    visited_score = [0] * (N + 1)
    visited = [False] * (N+1)

    queue = deque()

    queue.append(person)
    visited_score[person] += 1
    visited[person] = True
    time = 0

    while queue:
        current_node = queue.popleft()
        neighbors = graph[current_node]

        time += 1

        for i in neighbors:
            if not visited[i]:
                queue.append(i)
                visited_score[i] += time
                visited[i] = True
            else:
                original_score = visited_score[i]
                this_score =

    kv_list.append((sum(visited_score) - 1, person))

kv_list.sort()
print(kv_list)