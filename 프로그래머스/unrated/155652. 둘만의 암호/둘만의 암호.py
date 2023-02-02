def solution(s, skip, index):
    answer=[]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    for i in range(len(skip)):
        alphabet.remove(skip[i])
    for i in s:
        for j in range(len(alphabet)):
            if i==alphabet[j]:
                if j+index+1>len(alphabet):
                    answer.append(alphabet[(j+index)%len(alphabet)])
                else:
                    answer.append(alphabet[j+index])
                break
    str=''.join(answer)
    return str
