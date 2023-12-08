n, k = map(int, input().split())
from collections import deque

s = []
answer = deque()
for i in range(n):
    s.append(i + 1)
index = k - 1
for _ in range(n):
    if len(s) <= index:
        index = index % len(s)
    answer.append(s.pop(index))
    index = index + k - 1
print("<", end="")
print(", ".join(map(str, answer)), end="")
print(">", end="")
