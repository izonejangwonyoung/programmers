def solution(a, b):
    a.sort()
    b.sort()
    b.reverse()
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
