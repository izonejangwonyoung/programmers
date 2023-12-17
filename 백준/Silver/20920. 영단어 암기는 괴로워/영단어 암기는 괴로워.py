from collections import Counter
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
word_list = []
tmp_list = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.append(word)
# 1. 자주 나오는 단어일수록 앞에 배치한다
for d, c in Counter(word_list).most_common():
    if len(d) >= M:
        tmp_list[d] = c

# 2.해당 단어의 길이가 길수록 앞에 배치한다.
# print(tmp_list.values())
tmp_list = sorted(tmp_list.items(), key=lambda x: (-x[1], -len(x[0]),x[0]))

for i in tmp_list:
    print(i[0])
