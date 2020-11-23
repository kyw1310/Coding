def solution(gems):
    answer = []
    
    # 앞에서부터 모든 보석을 하나씩 가지게 될 때까지 오른쪽으로 이동 (0,1) start=0 end=1 -> (0,2) start=0 end=2 -> ...  
    # 만약 start지점에 있는 보석의 갯수가 두개라면 start를 오른쪽으로 이동시킨다
    # start 지점의 보석이 두개가 아니라면 그때의 start~end까지의 길이를 재고 가장 짧은 거리와 비교 후 현재까지의 가장 짧은 거리보다 짧을 경우 교체
    # 위와 같은 방법을 반복하면서 끝까지 체크 후 가장 짧은 길이를 
    
    x=set(gems)
    dic={}
    for i in x:
        dic[i]=0
    start=0
    end=0
    min_val=len(gems)+1
    for i in range(len(gems)):
        end+=1
        dic[gems[i]]+=1
        if 0 in dic.values():
            continue
        else:
            
            while True:
                if dic[gems[start]] >=2:
                    dic[gems[start]]-=1
                    start+=1
                    
                else:
                    if end-start < min_val:
                        min_val=end-start
                        answer=[start+1,end]
                    dic[gems[start]]-=1
                    start+=1
                    
                    break
    
    
    return answer
