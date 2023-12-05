n = int(input())
start = list(map(int, input().split()))
tmp = []
number = 1
while start:
    if number == start[0]:  # 찾고 있는 숫자를 발견했으면
        start.pop(0)
        # print("찾는 숫자:", number, "임시줄:", tmp, "시작줄", start)
        number += 1
    else:  # 아니라면
        if len(tmp) != 0:  # 임시 줄이 비어있지 않았을 떄
            if number == tmp[-1]:
                tmp.pop()
                number += 1
                # print("임시줄:", tmp, "시작줄", start)
            elif tmp[-1] < start[0]:  # 임시줄의 마지막 놈이 나보다 작은 경우에
                # print("임시줄:", tmp, "시작줄", start)
                print("Sad")
                break
            else:
                tmp.append(start.pop(0))
                # print("임시줄:", tmp, "시작줄", start)
        else:  # 임시 줄이 비어있다면
            tmp.append(start.pop(0))
            # print("임시줄:", tmp, "시작줄", start)

else:
    print("Nice")
