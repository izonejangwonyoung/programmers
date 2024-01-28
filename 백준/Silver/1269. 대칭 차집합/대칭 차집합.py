import sys

n, m = map(int, sys.stdin.readline().split())
list_a = set(map(int, sys.stdin.readline().split()))
list_b = set(map(int, sys.stdin.readline().split()))
a = list_b - list_a
b = list_a - list_b

print(len(a)+len(b))