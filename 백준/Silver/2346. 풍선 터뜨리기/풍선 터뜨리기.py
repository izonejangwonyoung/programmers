import sys
from collections import deque

answer = []  # 지워진 것들을 기록하는 곳
s = deque()
n = int(input())
s_list = deque(map(int, sys.stdin.readline().split()))
for i in range(n):
    s.append(i + 1)

if len(s) == 1:
    print('1')
else:
    answer.append(s.popleft())

    for _ in range(n):
        i = s_list.popleft()
        if i > 0:
            s.rotate(-(i - 1))
            s_list.rotate(-(i - 1))
            answer.append(s.popleft())
        else:
            s.rotate(-i)
            s_list.rotate(-i)
            answer.append(s.popleft())
        if not s:
            for i, k in enumerate(answer):
                if i == len(answer) - 1:  # 맨 뒤 요소인 경우
                    print(k, end="")
                else:
                    print(k, end=" ")
            break
