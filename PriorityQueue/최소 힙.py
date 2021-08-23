# https://www.acmicpc.net/problem/1927
import heapq, sys
N = int(input())
heap_list = []

for _ in range(N):
    element = int(sys.stdin.readline().rstrip())

    if element != 0:
        heapq.heappush(heap_list, element)

    else:
        if len(heap_list) == 0:
            print(0)
        else:
            pop_element = heapq.heappop(heap_list)
            print(pop_element)