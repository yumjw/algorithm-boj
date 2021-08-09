## sys.stdin.readline을 잘 쓰자
## 재귀할때는 recursive 풀어줘라.ㅇ

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

nodes = list(range(1, N+1))


def dfs(start_node):
    visited[start_node] = True
    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)

for i in nodes:
    if not visited[i]:
        dfs(i)
        count += 1

print(count)