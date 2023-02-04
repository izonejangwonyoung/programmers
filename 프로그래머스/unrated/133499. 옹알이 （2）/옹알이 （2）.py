# 얘네가 가능한 발음은 aya ye woo ma만 가능하다
# 같은 발음이 연속되면 안된다
import re

source=['aya','ye','woo','ma']

def solution(babbling):
    count=0
    for i in range(len(babbling)):
        babbling[i]=babbling[i].replace('aya','1')
        babbling[i] = babbling[i].replace('ye', '2')
        babbling[i] = babbling[i].replace('woo', '3')
        babbling[i] = babbling[i].replace('ma', '4')
    print(babbling)
    for i in range(len(babbling)):
        if babbling[i].isdigit()==True:  #숫자로만 이루어져있니?
            for j in range(len(babbling[i])-1):
                if babbling[i][j]==babbling[i][j+1]:
                    count-=1
                    break

            print('count')
            count+=1
    return count
