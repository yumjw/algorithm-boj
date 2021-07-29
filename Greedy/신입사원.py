# 시간초과 주의, list에 넣지 말고 그 전 최근 값을 기억하면 된다.
# Max나 Min값 같은게 필요한 경우 리스트에서 매번 구하는 것보단 변수에 저장해놓고 업데이트하자.
import sys

T = int(input())

for i in range(T):

    N = int(input())
    applicant_list = []
    count = 1

    for j in range(N):
        applicant = list(map(int, sys.stdin.readline().split()))
        applicant_list.append(applicant)

    applicant_list.sort()
    max_value = applicant_list[0][1]

    for cv_rank in range(1, N):
        interview_rank = applicant_list[cv_rank][1]
        if max_value > interview_rank:
            count += 1
            max_value = interview_rank

    print(count)