def solution(s):
    a = s.split(' ')
    a=list(map(int,a))
    return f"{min(a)} {max(a)}"

