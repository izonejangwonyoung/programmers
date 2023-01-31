def solution(s):
    alphabet_array = []
    for i in s:
        temp = ord(i) - 96
        alphabet_array.append(temp)
    answer = []
    temp2 = 0
    # answer.append(-1)
    for i in range(0, len(alphabet_array)):
        checksum=0
        for j in range(i - 1, -1, -1):
            if alphabet_array[j] == alphabet_array[i]:
                temp2 = i - j
                checksum = 1
                break
        if checksum == 0:  #같은 숫자 없이 새로 나온 숫자일 경우
            answer.append(-1)
        else:
            answer.append(temp2)
    # while 0 in answer:
    #     answer.remove(0)  # 'Smith' 삭제
    return answer