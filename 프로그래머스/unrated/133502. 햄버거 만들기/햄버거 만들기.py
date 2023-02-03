    
def solution(ingredient):
    answer=[1,2,3,1]
    stack=[]
    result=0
    for x in ingredient:
        stack.append(x)
        if stack[-4:]==answer:
            result+=1
            for _ in range(4):
                stack.pop()


    return result    
    
