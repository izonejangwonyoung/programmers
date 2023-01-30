def count(i,limit,power):
    cnt=0
    for k in range(1,int(i**(1/2))+1):
            if i%k==0:
                if k==i//k:
                    cnt+=1
                else:
                    cnt+=2
            if cnt>limit:
                return power
    return cnt

def solution(number,limit,power):
    total=1
    for i in range(2,number+1):
        lenman=count(i,limit,power)
        total+=lenman
    return total