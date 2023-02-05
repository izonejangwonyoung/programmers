from collections import Counter

example = [(2, 3), (3, 4), (2, 4)]


def solution(weights):
    answer = 0
    counter = Counter(weights)
    print(counter)
    print(counter.items())
    for weight, num in counter.items():
        answer += num * (num - 1) // 2
        for dis1, dis2 in example:
            print(dis1,dis2)
            answer += counter[weight * dis1 / dis2] * num
    return answer

