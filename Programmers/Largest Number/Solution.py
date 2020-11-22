def solution(numbers):
    str_numbers=list(map(str,numbers))
    
    # numbers 의 원소가 0~1000 이하 숫자이므로 자리수는 최대 4까지이다 따라서 원소자리수로 나눈 나머지로 나누게 됐을 경우 자동으로 앞에서부터 반복된다.
    
    result=''.join(sorted(str_numbers,key=lambda x: (x[0%len(x)],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True))
    if result=='0'*len(result):
        return '0'
    else:
        return result
