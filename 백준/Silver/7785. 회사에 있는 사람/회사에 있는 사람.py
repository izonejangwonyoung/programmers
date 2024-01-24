import sys

enter_list = set()
n = int(sys.stdin.readline())
for i in range(n):
    name, status = map(str, sys.stdin.readline().split())
    if status == "enter":
        enter_list.add(name)
    if status == "leave":
        enter_list.remove(name)
enter_list=sorted(enter_list,reverse=True)
for index, element in enumerate(enter_list):
    print(element, end='\n' if index < len(enter_list) - 1 else '')
