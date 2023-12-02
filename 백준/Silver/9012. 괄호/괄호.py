n = int(input())
for _ in range(n):
    left=[]
    k = list(input().strip())  # strip() 함수를 사용하여 문자열 앞뒤의 공백을 제거
    for i in range(len(k)):
        if k[i] == "(":
            left.append(k[i])
        elif k[i] == ")":
            if left:
                left.pop()
            else:  # 비었으면
                print("NO")
                break
    else:

        if not left:
            print("YES")
        else:
            print("NO")
