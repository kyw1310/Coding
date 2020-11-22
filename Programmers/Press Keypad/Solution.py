def solution(numbers, hand):
    answer = ''
    
    # 모든 키패드의 위치를 2차원 위의 포인트로 바꾼 후 현재 왼손 , 오른손의 위치와 다음 눌러야할 버튼의 거리를 비교 한 후 왼손 혹은 오른손을 옮겨가고 그 좌표를 저장하는 방식으로 진행 
    
    map=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    dic={}
    for row in range(len(map)):
        for col in range(len(map[row])):
            dic[map[row][col]]=[row,col]
    left=dic['*']
    right=dic['#']
    n=None
    n_=None
    u=None
    for i in numbers:
        n=i
        n_=dic[n]
        if n in [1,4,7]:
            u='L'
            left=dic[n]
        elif n in [3,6,9]:
            u='R'
            right=dic[n]
        else:
            if abs(n_[0]-left[0])+abs(n_[1]-left[1])<abs(n_[0]-right[0])+abs(n_[1]-right[1]):
                u='L'
                left=dic[n]
            elif abs(n_[0]-left[0])+abs(n_[1]-left[1])>abs(n_[0]-right[0])+abs(n_[1]-right[1]):
                u='R'
                right=dic[n]
            else:
                if hand=='right':
                    u='R'
                    right=dic[n]
                else:
                    u='L'
                    left=dic[n]
                    
        answer+=u
    return answer
