# https://www.acmicpc.net/problem/9205
import sys
from collections import deque

# t = int(sys.stdin.readline().rstrip())

N = int(sys.stdin.readline().rstrip())
bottles = 20

start_x, start_y = map(int, sys.stdin.readline().rstrip().split())
store_x, store_y = map(int, sys.stdin.readline().rstrip().split())
end_x, end_y = map(int, sys.stdin.readline().rstrip().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

half_length = 32768
graph = [[0]*(half_length*2) for _ in range(half_length*2)]
queue = deque()

queue.append([start_x, start_y])
graph[start_y+half_length][start_x+half_length] += 1

