def solution(n, computers):
    answer = 0
    #그래프 만들기
    graph={}
    for i in range(len(computers)):
        link=[]
        for j in range(len(computers[i])):
            if j!=i and computers[i][j]==1:
                link.append(j)
        graph[i]=link
    
    #bfs구현
    def bfs(graph,start_node):
        visit=[]
        queue=[]
        
        queue.append(start_node)
        
        while queue:
            node=queue.pop(0)
            if node not in visit:
                visit.append(node)
                queue.extend(graph[node])
        return visit
    
    
    network=[]
    for i in range(n):
        if set(network)==set(range(n)):
            break
        if i not in network:
            answer+=1
            network.extend(bfs(graph,i))
    
    
    
    return answer
