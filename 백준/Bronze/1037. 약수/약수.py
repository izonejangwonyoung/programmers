n = int(input())

s_list = list(map(int, input().split()))
max_value = 2
min_value = 1000000
if len(s_list) == 1 and s_list[0] % 2 == 1:
    max_value = s_list[0] * s_list[0]
    print(max_value)
else:
    for i in s_list:
        if max_value < i:
            max_value = i
        if min_value > i:
            min_value = i
    if max_value % 2 == 1:
        print(max_value * min_value)
    else:
        print(max_value * 2)
