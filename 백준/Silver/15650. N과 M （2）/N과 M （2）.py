import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

lliist = []
ans = set()


def back():
    if len(lliist) == m:
        # print(" ".join(map(str, lliist)))
        ans.add(" ".join(map(str, sorted(lliist))))
        return
    for i in range(1, n + 1, 1):
        if i not in lliist:
            lliist.append(i)
            back()
            lliist.pop()


back()
ans = sorted(ans)
print("\n".join(map(str, ans)))
