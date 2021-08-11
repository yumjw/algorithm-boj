from collections import deque
from copy import deepcopy

def palindrome(word):
    length = len(word)
    # 들어온 단어 길이가 홀수일 때
    if length % 2 == 1:
        # 가운데 기준으로 회문이거나
        half_index = length // 2
        queue = deque()
        for i in word[:half_index]:
            queue.append(i)
        if list(queue) == word[half_index+1:]:
            return 0

        # 회문이 아니면 홀수 유사 회문인지 확인
        else:
            word_list = list(word)
            for idx, element in enumerate(word_list):
                test_copy = deepcopy(word_list)
                

    # 들어온 단어 길이가 짝수일 때
    else:
        # 그 자체로 회문이거나
        half_index = length // 2
        queue = deque()
        for i in word[:half_index]:
            queue.append(i)
        if list(queue) == word[half_index:]:
            return 0
        # 하나 빼서 홀수 기준으로 양 옆이 똑같은지 확인
        else:
            pass