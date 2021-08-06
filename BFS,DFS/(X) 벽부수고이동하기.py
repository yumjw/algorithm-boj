from collections import deque
import copy
import sys

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방문 확인용 배열
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
# 인풋으로 받을 배열
field = []

for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().strip())))

queue = deque()

# 시작점이 완료점일 경우
if N == 1 and M == 1 and field[0][0] == 0:
    print(1)
else:
    visited[0][0][0] = 1
    queue.append([0, 0, 0])

    flag = 0
    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            ndr = x + dr[i]
            ndc = y + dc[i]

            # 범위안에 들어옴
            if 0 <= ndr < N and 0 <= ndc < M and visited[z][ndr][ndc] == 0:

                c = 0
                # 벽을 만났는데 아직 벽을 안뚫어봄
                if field[ndr][ndc] == 1 and z == 0:
                    visited[1][ndr][ndc] = visited[0][x][y] + 1
                    queue.append([ndr, ndc, 1])
                    c = 1

                # 벽 안만남 (길을 만난 경우)
                elif field[ndr][ndc] == 0:
                    visited[z][ndr][ndc] = visited[z][x][y] + 1
                    queue.append([ndr, ndc, z])

                # 도착한 경우
                if ndr == N - 1 and ndc == M - 1:
                    print(visited[z][ndr][ndc])
                    flag = 1
                    break

        if flag == 1:
            break

    if flag == 0:
        print(-1)




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