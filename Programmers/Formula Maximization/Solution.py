import itertools
def solution(expression):
    answer = 0
    results=[]
    
    # 연산 순위를 permutation으로 섞어주고 연산 순위에 따라 문자를 split 하고 연산순서대로 연산 진행 후 results에 담은 후 가장 큰 값을 return한다.
    
    # example ) 100-200*300-500+20 같은 경우 우선순위를 + - * 순이라고 한다면
    # 3순위로 먼저 split 진행 -> [100-200 , 300-500+20]
    # 2순위로 split 진행 -> [ [100,200] , [300,500+20] ]
    # 내부 연산 수행 -> [ [100,200] , [300,520] ]
    # 2순위를 중간에 삽입 -> [100-200 , 300-520]
    # 내부 연산 수행 -> [-100 , -220]
    # 3순위를 중간에 삽입 -> [-100 * -220 ]
    # 연산 후 절대값으로 results에 담는다.
    
    for v in itertools.permutations(['+','-','*'],3):
        second=v[1]
        third=v[2]
        one=expression.split(third)
        two=[]
        for r in one:
            two.append(r.split(second))
        for j in range(len(two)):
            for k in range(len(two[j])):
                two[j][k]=str(eval(two[j][k]))
        three=[]
        for i in range(len(two)):
            three.append(second.join(two[i]))
        for q in range(len(three)):
            three[q]=str(eval(three[q]))
        result=abs(eval(third.join(three)))
        results.append(result)
    answer=max(results)
    
    return answer
