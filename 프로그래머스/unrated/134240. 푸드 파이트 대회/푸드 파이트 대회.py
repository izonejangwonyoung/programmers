def solution(food):
    temp = []
    answer = []
    rev_answer=[]
    for i in range(len(food)):
        for k in range(food[i]):
            temp.append(i + 1)

    for i in range(1, max(temp) + 1):
        if temp.count(i) == 1:
            pass
        else:
            for j in range(temp.count(i) // 2):
                answer.append(i-1)

    rev_answer = answer[::-1]
    answer.append(0)
    result=[]
    result=answer+rev_answer
    str1=''.join(str(s) for s in result)
    return str1


