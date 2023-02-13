def solution(board, moves):
    empty = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                empty.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return check_result(empty) 

def check_result(empty):
    count = 0
    stack = []
    for i in empty:
        if stack and stack[-1] == i:
            stack.pop()
            count += 2
        else:
            stack.append(i)
    return count




#위에는 chatgpt가 리팩토링한 버전
#아래부터는 내가 작성한 코드

def solution(board, moves):
    empty = []
    counter = 0
    for i in moves:
        checker = 0
        counter += 1
        print(i, '번 째 열 탐색 시작')
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                print(board[j][i - 1], ' check')
                empty.append(board[j][i - 1])
                board[j][i - 1] = 0
                checker = 1
                break
        if checker == 0:  # 그 라인 인형이 아예 없는 경우
            continue
    a=check_result(empty)*2
    return a


global func_count
func_count = 0


def check_result(empty):
    global func_count, temp
    for i in range(1, len(empty)):
        print('현재 empty 구성:',empty)
        print('현재 empty 길이:',len(empty))
        print(i - 1, i)
        print(empty)
        if i>=len(empty):
            break
        if empty[i - 1] == empty[i]:
            print('겹치는 항목 발견')
            del empty[i - 1]
            del empty[i - 1]
            temp = empty.copy()
            func_count += 1
            check_result(empty)
    if temp == empty:
        print(func_count)
        return func_count

