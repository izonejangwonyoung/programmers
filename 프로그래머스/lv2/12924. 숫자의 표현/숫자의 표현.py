def solution(n):
    sum = 0
    count = 0
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            sum += j
            if sum>n:
                break
            if sum == n:
                count += 1
                break
        sum=0
    return count
