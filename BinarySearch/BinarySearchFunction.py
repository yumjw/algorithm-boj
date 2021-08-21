def binary_search(array, target_value, start_idx, end_idx):
    if start_idx > end_idx: # 정답이 없다: 재귀의 반복을 통해 start=end 상태 직후 start+1 = mid가 됨
        return None
    mid = (start_idx + end_idx) // 2 # 적당히 mid값을 찾는다
    if array[mid] == target_value: # 정확히 원하는 타겟값을 찾았다
        return mid
    elif array[mid] < target_value:
        return binary_search(array, target_value, mid + 1, end_idx)
    else:
        return binary_search(array, target_value, start_idx, mid - 1)