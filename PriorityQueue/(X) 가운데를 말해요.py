import heapq, sys, bisect

N = int(sys.stdin.readline().rstrip())
lst = []
num = 0

for i in range(N):
    num += 1
    element = int(sys.stdin.readline().rstrip())
    heapq.heappush(lst, element)

    nsmallest_index = num//2
    temp_list = heapq.nsmallest(nsmallest_index+1, lst)
    print(temp_list[i//2])