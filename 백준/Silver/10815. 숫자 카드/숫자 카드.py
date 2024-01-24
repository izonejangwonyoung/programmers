import sys

N = int(input())
have_list = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
search_list = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(search_list)):
    if search_list[i] in have_list:
        print(1, end='')
        if i < len(search_list)-1:
            print(' ',end='')
    else:
        print(0, end='')
        if i < len(search_list)-1:
            print(' ',end='')