res=[]
def solution(n, source=1, auxiliary=2, target=3):    
    if n == 1:
        res.append([source,target])
        return
    solution(n - 1, source, target, auxiliary)
    res.append([source,target])
    solution(n - 1, auxiliary, source, target)
    return res
