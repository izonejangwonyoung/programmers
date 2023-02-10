from itertools import combinations

global count


def solution(number):
    global count
    count = 0
    a = list(combinations(number, 3))
    value = len(a)

    for i in range(value):
        # print(sum(a[i]))
        if sum(a[i]) == 0:
            print('check')
            count += 1

    return count
