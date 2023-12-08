
n = int(input())  # 명령의 개수
from collections import deque
import sys
s = deque()
for _ in range(n):
    order = list(map(int, sys.stdin.readline().strip().split()))
    if order[0] == 1:
        s.appendleft(order[1])
    elif order[0] == 2:
        s.append(order[1])
    elif order[0] == 3:
        if s:
            print(s.popleft())
        else:
            print(-1)
    elif order[0] == 4:
        if s:
            print(s.pop())
        else:
            print(-1)

    elif order[0] == 5:
        print(len(s))
    elif order[0] == 6:
        if s:
            print(0)
        else:
            print(1)

    elif order[0] == 7:
        if s:
            print(s[0])
        else:
            print(-1)
    elif order[0] == 8:
        if s:
            print(s[-1])
        else:
            print(-1)
