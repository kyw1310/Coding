def minion_game(string):
    
    
    vowel=['A','I','E','O','U']
    string_length=len(string)
    
    # string S가 가질 수 있는 substring의 갯수는 총 n*(n+1) / 2 개 이다.
    
    total_substring=int((string_length*(string_length+1))/2)
    
    kevin=0
    stuart=0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin=kevin+(string_length-i)
    # i의 위치에서 만들 수 있는 substring 의 갯수는 (전체길이 - i)개 이므로 모음에 들어갈 경우만 카운트해서 kevin에 담고 전체에서 kevin을 빼면 stuart를 알 수 있다.
    
    stuart=total_substring-kevin
    
    if stuart> kevin:
        print('Stuart',stuart)
    elif stuart < kevin:
        print('Kevin',kevin)
    else:
        print('Draw')

