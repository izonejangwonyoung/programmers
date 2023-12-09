from collections import deque

N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
M = int(input())
list_C = list(map(int, input().split()))
answer = deque()
for i in range(len(list_A) - 1, -1, -1):
    if list_A[i] == 0:
        answer.append(list_B[i])

for i in list_C:
    answer.append(i)

for i in range(M - 1):
    print(answer[i], end=" ")
print(answer[M - 1], end='')