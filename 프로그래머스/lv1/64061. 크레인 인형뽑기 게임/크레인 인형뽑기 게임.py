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
