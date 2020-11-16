def minion_game(string):
    aa=['A','I','E','O','U']
    le=len(string)
    total=int((le*(le+1))/2)
    
    b=0
    a=0
    for i in range(len(string)):
        if string[i] in aa:
            b=b+(le-i)
    
    a=total-b
    
    if a> b:
        print('Stuart',a)
    elif a < b:
        print('Kevin',b)
    else:
        print('Draw')
    # your code goes here

