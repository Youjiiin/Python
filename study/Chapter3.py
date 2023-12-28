from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미
from random import random, randint, randrange
# import math 도 가능한데 대신에 사용 기능앞에 math. 를 작성해줘야 함

num = 2.123

# 숫자 처리 함수
print(abs(num)) # 절대값 
print(pow(num, 2)) # 앞을 뒤만큼 거듭제곱
print(round(num, 2)) # 앞을 반올림, 뒤는 소수점 이하 자릿수
print("-----------------------")

# math 모듈
print(floor(num)) # 내림
print(ceil(num)) # 올림
print(sqrt(num)) # 제곱근
print(random())
print(int(random() * 10) + 1)
print(randint(1, 10)) # 10이하
print(randrange(1, 11)) # 11미만
print("-----------------------")


date = randint(4, 28)
print(date)