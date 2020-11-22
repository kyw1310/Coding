def solution(begin, target, words):
    answer = 0
    
    # 한번의 탐색으로 도달할 수 있는 모든 단어들의 리스트 탐색
    def search_next(graph,start_nodes):
        
        next=[]
        for node in range(len(start_nodes)):
            # 여러 노드들의 리스트에서 다음 노드로 도달 할 수 있는 노드들의 리스트를 구한다.
            # 단 중복된 노드는 탐색하지 않음
            if start_nodes[node] not in start_nodes[:node]:
                next.extend(graph[start_nodes[node]])
        print(next)
        
        return next
    
    
    # 그래프 생성 
    graph={}
    one=[]
    
    for i in range(len(words)):
        num=0
        for j in range(len(begin)):
            if begin[j]==words[i][j]:
                num+=1
        if num==len(begin)-1:
            one.append(words[i])
    graph[begin]=one
    
    for i in range(len(words)):
        link=[]
        for j in range(len(words)):
            num=0
            if i != j:
                for k in range(len(begin)):
                    if words[i][k]==words[j][k]:
                        num+=1
                if num==len(begin)-1:
                    link.append(words[j])
        graph[words[i]]=link
    
    
    # 타겟이 words 리스트 안에 없을 경우 도달 불가
    if target not in words:
        return 0
    else:
        # 만일 타겟이 words 리스트 안에 존재할 경우 탐색 시작
        next=search_next(graph,[begin])
        num=1
        while target not in next:
            # 만약 words의 리스트의 갯수보다 많이 탐색했지만 target에 도달하지 못한 경우 연결되어있지 않은 노드로 판단
            if num>len(words):
                return 0
            next=search_next(graph,next)
            num+=1
        return num
    
    
    
    
    return answer
