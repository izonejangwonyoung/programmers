import sys
from collections import deque

n = int(input())
s = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        tmp = int(order[1])
        s.append(tmp)
    else:
        if order[0] == "front":
            if not s:
                print(-1)
            else:
                print(s[0])
        elif order[0] == "back":
            if not s:
                print(-1)
            else:
                print(s[-1])
        elif order[0] == "empty":
            if not s:
                print(1)
            else:
                print(0)
        elif order[0] == "size":
            print(len(s))
        elif order[0] == "pop":
            if not s:
                print(-1)
            else:
                print(s.popleft())
