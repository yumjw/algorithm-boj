import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline().rstrip())

first_line = [i for i in range(1, N+1)]
first_line_checked = [False for _ in range(N)]
second_line = []

result = []

for _ in range(N):
    second_line.append(int(sys.stdin.readline().rstrip()))

def dfs(first_line_start_node_idx):
    next_first_line_value = second_line[first_line_start_node_idx]
    second_value_set.append(next_first_line_value)

    next_value_first_line_idx = next_first_line_value - 1

    if first_line[next_value_first_line_idx] not in first_value_set:
        first_value_set.append(first_line[next_value_first_line_idx])
        dfs(next_value_first_line_idx)
    else:
        return


for idx in range(N):
    if not first_line_checked[idx]:
        first_value_set = [idx + 1]
        second_value_set = []

        dfs(idx)
        if len(set(first_value_set)-set(second_value_set)) == 0:
            result.extend(first_value_set)
            for i in first_value_set:
                first_line_checked[i-1] = True

result.sort()
print(len(result))
for i in result:
    print(i)
