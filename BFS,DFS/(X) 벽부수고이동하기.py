from collections import deque
import copy
import sys






## 시간초과. 모든 벽을 부수는 경우에 하나씩에 대해서 BFS를 수행하면 안된다.
# N, M = map(int, input().split())
#
# origin_graph = []
# break_candidate = []
# min_distance = 1000000
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# for i in range(N):
#     row = list(map(int, sys.stdin.readline().rstrip()))
#     origin_graph.append(row)
#
#     for j, element in enumerate(row):
#         if element == 1:
#             break_candidate.append( [i, j] )
#
# for break_point in break_candidate:
#     try_graph = copy.deepcopy(origin_graph)
#     queue = deque()
#     visited = [([0] * M) for row in range(N)]
#
#     break_y, break_x = break_point
#
#     try_graph[break_y][break_x] = 0
#
#     queue.append([0,0])
#     visited[0][0] = 1
#     find = False
#
#     while queue:
#         y, x = queue.popleft()
#
#         for i in range(4):
#             new_y = y + dy[i]
#             new_x = x + dx[i]
#
#             if new_y == (N-1) and new_x == (M-1):
#                 distance = visited[y][x] + 1
#                 if min_distance > distance:
#                     min_distance = distance
#                     find = True
#                     break
#
#             if (0 <= new_y < N) and (0 <= new_x < M):
#                 if try_graph[new_y][new_x] == 0 and visited[new_y][new_x] == 0:
#                     queue.append([new_y, new_x])
#                     visited[new_y][new_x] = visited[y][x] + 1
#
#         if find:
#             break
#
# if find:
#     print(min_distance)
# else:
#     print(-1)