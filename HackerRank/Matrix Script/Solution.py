import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#문제에서 if문을 사용하지말고 re를 사용하게끔했으므로 정규표현식으로 찾는다.

p=re.compile('[a-zA-Z0-9][^a-zA-Z0-9]+[a-zA-Z0-9]')


result=''
for j in range(m):
    for i in range(n):
        result+=matrix[i][j]

#세로로 글자를 완성시킨 후 문자와 문자사이의 특수문자는 제거

kk=p.findall(result)

for i in range(len(kk)):
    result=result.replace(kk[i],kk[i][0]+' '+kk[i][-1])
print(result)

