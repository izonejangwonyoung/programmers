def option_one(original, n):
    if bin(n)[2:].count('1') == bin(original)[2:].count('1'):
        return True
    else:
        return False


def solution(n):
    original = n
    while True:
        n = n + 1
        if option_one(original, n):
            break
    return n
