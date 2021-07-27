# 시간초과 주의, list에 넣지 말고 그 전 최근 값을 기억하면 된다.
import sys

T = int(input())
for i in range(T):

    N = int(input())
    applicant_list = []
    count = 1

    for j in range(N):
        applicant = list(map(int, sys.stdin.readline().split()))
        applicant_list.append(applicant)

    max_value = applicant_list[0][1]

    for cv_rank in range(1, N):
        interview_rank = applicant_list[cv_rank][1]
        if max_value > interview_rank:
            count += 1
            max_value = interview_rank

    print(count)


# 정답

import sys

T = int(input())  # 테스트케이스

for i in range(0, T):
    Cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()  # 서류 기준 오름차순 정렬
    Max = people[0][1]

    for i in range(1, N):
        if Max > people[i][1]:
            Cnt += 1
            Max = people[i][1]

    print(Cnt)