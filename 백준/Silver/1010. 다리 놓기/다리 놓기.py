from math import trunc

t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))
    N = n[1]
    K = n[0]

    tmp1 = 1
    tmp2 = 1
    for i in range(N):
        tmp1 *= i + 1

    for j in range(N - K):
        tmp2 *= j + 1
    for k in range(K):
        tmp2 *= k + 1
    print(trunc(tmp1 / tmp2))