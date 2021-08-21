import sys

K, N = map(int, input().split())

original_lans = []

for i in range(K):
    original_lans.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(original_lans)

while start <= end:
    mid = (start+end)//2
    lines = 0

    for lan in original_lans:
        lines += lan // mid

    if lines >= N:
        start = mid + 1

    else:
        end = mid - 1

print(end)