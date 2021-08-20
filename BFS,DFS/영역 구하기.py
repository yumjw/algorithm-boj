import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, sys.stdin.readline().rstrip().split())

graph = [([0]*M) for _ in range(N)]
nodes = [(n, m) for n in range(N) for m in range(M)]

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

# (n, m)
for _ in range(K):
    start_n, start_m, end_n, end_m = map(int, sys.stdin.readline().rstrip().split())

    for n in range(start_n,end_n):
        for m in range(start_m,end_m):
            graph[n][m] = -1

result_list = []
count = 0

def dfs(n, m):
    graph[n][m] = 1
    global count
    count += 1

    for i in range(4):
        new_n = n + dn[i]
        new_m = m + dm[i]

        if 0 <= new_m < M and 0 <= new_n < N:
            if graph[new_n][new_m] == 0:
                dfs(new_n, new_m)


for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            count = 0
            dfs(n, m)
            result_list.append(count)

result_list.sort()
print(len(result_list))

for i in range(len(result_list)):
    print(result_list[i], end=' ')