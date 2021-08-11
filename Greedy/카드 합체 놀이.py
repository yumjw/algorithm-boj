import sys
n, m = map(int, input().split())
a_i = list(map(int, sys.stdin.readline().rstrip().split()))

# Using Priority Queue
import heapq
cards = []

for card in a_i:
    heapq.push(cards, card)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heapop(cards)

    heapq.heappush(cards, card1+card2)
    heapq.heappush(cards, card1+card2)
print(sum(cards))

## Using Binary Search
# import bisect
# a_i.sort()
#
# for i in range(m):
#
#     x = a_i.pop(0)
#     y = a_i.pop(0)
#     new_value = x+y
#
#     idx = bisect.bisect_left(a_i, new_value)
#     before = a_i[:idx]
#     after = a_i[idx:]
#
#     a_i = before + ([new_value]*2) + after
# print(sum(a_i))