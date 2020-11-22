def solution(brown, yellow):
    answer = []
    
    
    
    
    m=int(((4+brown)-((4+brown)**2-4*2*2*(yellow+brown))**(1/2))//4)
    n=int((yellow//(m-2))+2)
    
    if m>=n:
        answer=[m,n]
    else:
        answer=[n,m]
    
    
    
    return answer
