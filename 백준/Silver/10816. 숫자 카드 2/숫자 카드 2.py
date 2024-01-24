import sys
import collections

N = int(input())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))
dic_n = collections.Counter(N_list)
M = int(input())
M_list = list(map(int, sys.stdin.readline().rstrip().split()))
for i in M_list:
    if dic_n[i] != 0:
        print(dic_n[i],end=' ')
    else:
        print(0,end=' ')