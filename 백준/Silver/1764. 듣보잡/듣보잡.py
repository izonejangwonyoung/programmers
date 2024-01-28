import sys

N,M=map(int,sys.stdin.readline().rstrip().split())
count=0

answer_list=[]
not_listen_list=[]
not_see_list=set()

for i in range(N):
    not_listen_list.append(sys.stdin.readline().rstrip())

for i in range(M):
    not_see_list.add(sys.stdin.readline().rstrip())


for i in range(len(not_listen_list)):
    if not_listen_list[i] in not_see_list:
        count+=1
        answer_list.append(not_listen_list[i])

print(count)
sorted_answer_list=sorted(answer_list)
for i in sorted_answer_list:
    print(i)
