from collections import deque

N, L, R = map(int, input().split())

graph = []
one_time_united = []

for i in range(N):
    row = list(map(int, input().split()))
    row.append(graph)

visited = [([False]*N) for _ in range(N)]

