def solution(numbers, hand):
    answer = []
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left_start = keypad['*']
    right_start = keypad['#']
    for i in numbers:
        location = keypad[i]
        if i in [1, 4, 7]:
            left_start = location
            answer.append("L")

        elif i in [3, 6, 9]:
            right_start = location
            answer.append("R")
        else:
            left_d = 0
            right_d = 0

            for a, b, c in zip(left_start, right_start, location):
                left_d += abs(a - c)
                right_d += abs(b - c)
            if left_d < right_d:
                answer.append("L")
                left_start = location

            elif left_d > right_d:
                answer.append("R")
                right_start = location
            else:
                if hand == "right":
                    answer.append("R")
                    right_start = location
                else:
                    answer.append("L")
                    left_start = location
    answer="".join(answer)
    return answer
