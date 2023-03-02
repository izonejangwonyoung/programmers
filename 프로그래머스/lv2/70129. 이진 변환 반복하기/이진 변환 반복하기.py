import re


def solution(s):
    counter = 0
    rep_counter = 0
    while s != '1':
        counter += s.count('0')
        s = re.sub(r"0", "", s)
        # print('0을 제거한 s: ', s)
        s = len(s)
        s = bin(s)
        s = s[2:]
        rep_counter += 1

        # print("이진수 변환한 s: ", s)
    print(counter)
    return [rep_counter, counter]

