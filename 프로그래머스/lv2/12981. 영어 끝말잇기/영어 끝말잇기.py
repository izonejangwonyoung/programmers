import math


def solution(n, words):
    a=0
    stack = []
    count = 1
    stack.append(words[0])
    for i in range(1, len(words)):
        if words[i] in stack:
            print('op1')
            print(count)
            return [(i%n)+1,i//n+1]
        if words[i][0] != stack[-1][-1]:
            print('op2')
            print(words[i][0])
            print(stack[-1][-1])
            print(count)
            print(stack)
            a=(len(stack)+1)%n
            if (len(stack)+1)%n==0:
                a=((len(stack)+1)%n)+1
                print('a=',a)
            return [(i % n) + 1, i // n + 1]
        stack.append(words[i])
        print(words[i])
        count += 1
    return [0, 0]
