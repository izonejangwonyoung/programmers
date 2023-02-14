def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        left = survey[i][:1]  # 비동의
        right = survey[i][1:]  # 동의
        turn_choice = choices[i]

        if 1 <= turn_choice <= 3:
            dic[left] += 4-turn_choice
        if 4 < turn_choice:
            dic[right] += turn_choice-4

    answer = "".join(checkanswer(dic))
    return answer


def checkanswer(dic):
    list_key = list(dic.keys())
    list_val = list(dic.values())
    answer = []
    for i in range(0, len(list_val), 2):
        if list_val[i] < list_val[i + 1]:
            answer.append(list_key[i + 1])
        elif list_val[i] > list_val[i + 1]:
            answer.append(list_key[i])
        else:
            if ord(list_key[i]) > ord(list_key[i + 1]):
                answer.append(list_key[i + 1])
            else:
                answer.append(list_key[i])
    return "".join(answer)