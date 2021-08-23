import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
namu_list = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, max(namu_list)

while start <= end:
    mid = (start + end) // 2
    get_namu = 0

    for namu in namu_list:
        left = max([0, namu-mid])
        get_namu += left

    if get_namu >= M:
        start = mid + 1

    elif get_namu < M:
        end = mid - 1

print(end)