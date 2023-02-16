# def solution(cards1, cards2, goal):
#     checker = 0
#     a = 0
#     b = 0
#     for i in range(len(goal)):
#         print('-------------------')
#         print(i)
#         print(goal[i])
#         if cards1[0] == goal[i]:
#             print('here1')
#             print(cards1[0], goal[i])
#             cards1.pop(0)
#             print('card1:', cards1)
#         elif len(cards2) != 0 and cards2[0] == goal[i]:
#             print('here2')
#             print(cards2[0], goal[i])
#             cards2.pop(0)
#             print('card2:', cards2)
#         else:
#             checker=1
#     if checker == 1:
#         return "No"
#     if checker == 0:
#         return "Yes"
from collections import deque


def solution(cards1, cards2, goal):
    a = deque(goal)
    b = deque(cards1)
    c = deque(cards2)
    bb=b.popleft()
    cc=c.popleft()
    for i in range(len(a)):
        temp = a.popleft()
        if temp == bb:
            if len(b)>0:
                bb=b.popleft()
                print(b, c)
        elif temp ==cc:
            if len(c)>0:
                cc=c.popleft()
                print(b, c)
        else:
            return "No"

    return "Yes"
