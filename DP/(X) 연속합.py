import sys
sys.setrecursionlimit(10000)

n = int(input())
lst = list(map(int, input().split()))

idx = 0
max = lst[0]

while idx <= n-1:

    temp_sum = 0
    for i in range(idx, n):
        if lst[i] >= 0:
            temp_sum += lst[i]
            if max < temp_sum:
                max = temp_sum
                break
        else:
            current_minus = lst[i]
            after_plus_sum = 0
            temp_idx = i + 1

            while temp_idx <= n-1 and lst[temp_idx] > 0:
                after_plus_sum += lst[temp_idx]
                temp_idx += 1

            if after_plus_sum + current_minus > 0:
                temp_sum += after_plus_sum + current_minus
                if temp_sum > max:
                    max = temp_sum

                idx = temp_idx + 1
                break
            else:
                if after_plus_sum > max:
                    max = after_plus_sum
                idx = temp_idx + 1
                break

print(max)