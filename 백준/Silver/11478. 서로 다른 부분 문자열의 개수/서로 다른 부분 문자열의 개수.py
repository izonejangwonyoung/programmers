import sys

input_string = sys.stdin.readline().rstrip()
answer_list = set()
new_answer_list = []
for i in range(len(input_string) + 1):
    for j in range(len(input_string)):
        if j != j + i:
            answer_list.add(input_string[j:j + i])
        # print(j, j + i, input_string[j:j + i])
# for i in answer_list:
#     if len(i) > 0:
#         new_answer_list.append(sorted(i))

print(len(answer_list))
