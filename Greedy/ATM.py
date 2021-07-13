N = int(input())

total_time = 0
time_list = list(map(int, input().split()))

time_list.sort()

for idx, time in enumerate(time_list):
    total_time += sum(time_list[:idx+1])

print(total_time)