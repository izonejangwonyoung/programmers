def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]


def solution(k, m, score):
    score = sorted(score, reverse=True)
    score = list_chuck(score, m)
    temp = 0
    for i in range(0, len(score)):
        if len(score[i])==m:
            temp += min(score[i]) * m
    answer = temp
    return answer
