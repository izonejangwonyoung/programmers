M, N = map(int, input().split())
set_S = set()
target_list = []
count = 0
for i in range(M):
    set_S.add(input().rstrip())
for j in range(N):
    target_list.append(input().rstrip())
for k in range(N):
    if target_list[k] in set_S:
        count += 1

print(count,end='')