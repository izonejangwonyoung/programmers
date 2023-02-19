def solution(n, lost, reserve):

    templost=list(set(lost)-set(reserve))
    tempreserve=list(set(reserve)-set(lost))
    lost=templost
    reserve=tempreserve
    print(templost)
    print(tempreserve)

    for i in range(len(reserve)):
        possible_one = reserve[i] - 1
        possible_two = reserve[i] + 1
        if possible_one in lost:
            lost.remove(possible_one)
            print('here',lost)
            continue
        if possible_two in lost:
            lost.remove(possible_two)
            print('here2',lost)
            continue
    return n-len(lost)
