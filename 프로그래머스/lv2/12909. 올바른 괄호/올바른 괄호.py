def solution(s):
    lst = list(s)
    counter = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            counter += 1
        if lst[i] == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter>0:
        return False

    return True
