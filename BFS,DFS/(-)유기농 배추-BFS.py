from collections import deque

# T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())

count = 0
queue = deque()
coordinate_list = []

for i in range(K):
    x, y = map(int, input().split())
    coordinate_list.append((x,y))

