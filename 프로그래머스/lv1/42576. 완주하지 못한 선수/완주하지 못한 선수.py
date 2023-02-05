from collections import Counter


def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)

    for p_name in p_counter:
        if p_counter[p_name] != c_counter[p_name]:
            answer = p_name
    return answer
