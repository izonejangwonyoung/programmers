def solution(k, score):
    result = []  # 실제 제출해야하하는 정답 리스트
    temp = []  # k등 계산을 위한 임시 리스트
    if k>len(score):
        for i in range(len(score)):
            a=score[i]
            temp.append(a)
            temp=sorted(temp,reverse=True)
            result.append(temp[-1])
        return result
    
    for i in range(k):
        a=score[i]
        temp.append(a)
        temp=sorted(temp,reverse=True)
        result.append(temp[-1])

    for i in range(k, len(score)):
        temp.append(score[i])
        temp = sorted(temp,reverse=True)
        result.append(temp[k - 1])
    return result
