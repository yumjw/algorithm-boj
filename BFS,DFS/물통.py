from collections import deque

queue = deque()
A, B, C = map(int, input().split())

A_current = 0
B_current = 0
C_current = C

result = []
visited = [[False]*(B+1) for _ in range(A+1)]


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x,y))

queue.append((0, 0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    z = C-x-y
    if x == 0:
        result.append(z)

    water=min(x, B-y)
    pour(x-water, y+water)

    water=min(x, C-z)
    pour(x-water, y)

    water=min(y, A-x)
    pour(x+water, y-water)

    water=min(y, C-z)
    pour(x, y-water)

    water=min(z, A-x)
    pour(x+water, y)

    water=min(z, B-y)
    pour(x, y+water)

result.sort()
print(' '.join(map(str, result)))