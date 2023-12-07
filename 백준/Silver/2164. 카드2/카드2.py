from collections import deque

s = deque()

n = int(input())
for i in range(n):
    s.append(i + 1)
while True:
    if len(s) >= 2:
        s.popleft()
        if len(s) == 1:
            print(s[0])
            break
        else:
            s.append(s.popleft())
            if len(s) == 1:
                print(s[0])
                break
    else:
        print(s[0])
        break