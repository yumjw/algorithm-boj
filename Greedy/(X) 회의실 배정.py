# (접근 방법 틀림) 회의시간 짧은 애들 우선 배정하되 시간이 겹치면 앞순서로 배정한다
count = 0
N = int(input())

meeting_list = []
meeting_final = []

for i in range(N):
    meeting = list(map(int, input().split(' ')))
    meeting_obj = [meeting[1]-meeting[0]] + meeting
    meeting_list.append(meeting_obj)

meeting_list.sort()

for meeting in meeting_list:
    if len(meeting_final) == 0:
        meeting_final.append(meeting)
        count += 1


    else:
        add = True
        meeting_time = meeting_obj[0]
        meeting_start = meeting_obj[1]
        meeting_end = meeting_obj[2]

        for idx in range(0, len(meeting_final)):
            previous_meeting_start = meeting_final[idx][1]
            previous_meeting_end = meeting_final[idx][2]

            if (previous_meeting_start < meeting_start < previous_meeting_end) or (previous_meeting_start < meeting_end < previous_meeting_end):
                add = False
                break

        if add:
            count +=1
            meeting_final.append(meeting)

print(count)