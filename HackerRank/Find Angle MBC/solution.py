import math

n=int(input())
m=int(input())

# 직각삼각형에서 빗변의 중점과 B를 이으면 ( AM = BM = CM ) 이 된다.
# 그러므로 삼각형 MBC는 이등변삼각형이 되고 (왜냐하면 BM=CM) 각MBC=각MCB 가 되므로 tan(theta) = AB/BC가 된다. 그러므로 theta = atan(AB/BC)가 된다.


s=n/m




print(str(round(math.degrees(math.atan(s))))+'°')
