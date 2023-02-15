from collections import Counter


def solution(id_list, report, k):
    x = {}
    victim = []
    suspect_list = []
    suspect = []
    punish_people = []
    answer = []
    report = set(report)
    for i in id_list:
        x.setdefault(i, 0)  # 딕셔너리에 채워넣기
    for i in report:
        temp = i.split()
        victim.append(temp[0])
        suspect.append(temp[1])
    suspect_name = list(Counter(suspect).keys())
    suspect_count = list(Counter(suspect).values())
    for i in range(len(suspect_count)):
        if suspect_count[i] >= k:
            punish_people.append(suspect_name[i])

    for i in range(len(suspect)):
        if suspect[i] in punish_people:
            answer.append(victim[i])

    real_answer = []
    for i in range(len(id_list)):
        real_answer.append(0)
    for i in range(len(answer)):
        tempvalue = id_list.index(answer[i])
        real_answer[tempvalue] += 1


    return real_answer

