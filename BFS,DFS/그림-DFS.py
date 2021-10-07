# https://www.acmicpc.net/problem/1926
import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().rstrip())
num = 0
pictures = []

visited = [[False]*m for _ in range(n)]
graph = []
nodes = [(y, x) for y in range(n) for x in range(m)]


for _ in range(n):
    row = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(row)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(start_node):
    y, x = start_node
    visited[y][x] = True

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if 0 <= new_y < n and 0 <= new_x < m:
            if not visited[new_y][new_x]:
                dfs([new_y, new_x])

for node in nodes:
    y, x = node
    if not visited[y][x]:
        visited[y][x] = True
        num += 1