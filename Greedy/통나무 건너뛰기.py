## idea는 Okay. 근데 로직을 다시 보자.

import sys

N = int(input())
namu_list = list(map(int, sys.stdin.readline().split()))

namu_list.sort()
if len(namu_list) % 2 == 1:
    namu_list.append(namu_list[-1])

namu_length = len(namu_list)

odd_list = []
odd_max = 1000000000

even_list = []
even_max = 1000000000

candidate_list = []

while namu_list:
    namu = namu_list.pop()
    if namu_length % 2 == 0:
        even_list.append(namu)
    else:
        odd_list.append(namu)
    namu_length -= 1

candidate_list.append(abs(odd_list[-1]-even_list[-1]))

for odd_idx in range(len(odd_list)-1):
    odd_comparer = odd_list[odd_idx] - odd_list[odd_idx + 1]
    if odd_max > odd_comparer:
        odd_max = odd_comparer

for even_idx in range(len(even_list)-1):
    even_comparer = even_list[even_idx] - odd_list[even_idx + 1]
    if even_max > even_comparer:
        even_max = even_comparer

candidate_list.append(odd_max)
candidate_list.append(even_max)

print(max(candidate_list))