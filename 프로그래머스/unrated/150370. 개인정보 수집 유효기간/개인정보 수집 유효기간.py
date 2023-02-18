from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    today_year = today.split('.')[0]
    today_month = today.split('.')[1]
    today_day = today.split('.')[2]
    term_dict = {}
    temp_answer = []
    real_now_policy = []
    answer = []
    diff_dayList = []
    for i in range(len(terms)):
        term_dict[terms[i].split(' ')[0]] = terms[i].split(' ')[1]
    for i in range(len(privacies)):
        now_policy = privacies[i].split()[1]
        real_now_policy.append(term_dict[now_policy])
        diff_year = int(today_year) - int(privacies[i].split(' ')[0].split('.')[0])
        dif_month = int(today_month) - int(privacies[i].split(' ')[0].split('.')[1])
        diff_day = int(today_day) - int(privacies[i].split(' ')[0].split('.')[2])
        diff_dayList.append(diff_day)
        total_diff_month = 12 * diff_year + dif_month
        # if int(today_day) > int(privacies[i].split(' ')[0].split('.')[2]):
        if int(diff_day) < 0:
            total_diff_month = total_diff_month - 1
            temp_answer.append(total_diff_month)
        else:
            temp_answer.append(total_diff_month)
    for i in range(len(temp_answer)):
        if int(temp_answer[i]) >= int(real_now_policy[i]):
            answer.append(i + 1)

    return answer
