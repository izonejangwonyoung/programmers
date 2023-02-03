answer = 0  # 받은 콜라의 수

import sys
sys.setrecursionlimit(10000)
def solution(a, b, n):
    global answer
    if n < a:
        return answer
    if n % a == 0:  # 나누어떨어진면
        temp = (n // a)*b
        answer += (n // a)*b
    else:  # 나누어떨어지지않으면
        temp = ((n // a)*b) + (n % a)
        answer += (n // a)*b
    solution(a, b, temp)
    return answer

