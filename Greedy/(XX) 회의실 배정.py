# 재풀이 해서도 틀림
import sys

N = int(input())
meeting_list = []

for i in range(N):
    meeting = list(map(int, sys.stdin.readline().rstrip().split()))
    meeting_obj = [meeting[0], meeting[1]]
    meeting_list.append(meeting_obj)

meeting_list.sort(key=lambda x:(x[1], x[0]))

count = 1
end_time=meeting_list[0][1]

for i in range(1, N):
    if meeting_list[i][0] >= end_time:
        count += 1
        end_time = meeting_list[i][1]

print(count)