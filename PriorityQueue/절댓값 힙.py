import heapq, sys

N = int(sys.stdin.readline().rstrip())

def return_sigh(x):
    if x > 0:
        return 1
    else:
        return -1

lst = []

for _ in range(N):

    element = int(sys.stdin.readline().rstrip())

    if element != 0:
        heapq.heappush(lst, [abs(element), return_sigh(element)])

    else:
        if len(lst) == 0:
            print(0)
        else:
            poped_element_pair = heapq.heappop(lst)
            print(poped_element_pair[0]*poped_element_pair[1])