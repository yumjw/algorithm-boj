N = int(input())
rope_list = []

for i in range(N):
    rope_list.append(int(input()))

rope_list.sort(reverse=True)
minimum_weight_list = []

for idx, rope in enumerate(range(len(rope_list))):
    current_rope_weight = rope_list[idx] * (idx+1)
    minimum_weight_list.append(current_rope_weight)

print(max(minimum_weight_list))