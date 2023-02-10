from collections import Counter



def check2(X, Y):
    a =(Counter(X) - (Counter(X) - Counter(Y)))
    a=list(a.elements())
    return a


def solution(X, Y):
    example = 0
    count = 0
    answer = check2(X, Y)
    answer = sorted(answer, reverse=True)
    example = "".join(answer)
    if not answer:
        example = "-1"
        return example

    if answer[0] == "0":
        example = "0"
        return example
    str(example)
    return example
