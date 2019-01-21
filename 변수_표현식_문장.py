#Constants : 상수는 변하지 않는 값으로 출력된다. (정수(inits), 실수(floats)모두 동일하다.)
#이를테면,

print(123) #123으로 값을 출력, 123이 Constant
print(98.6) #98.6을 출력, 98.6은 Constant
print('Hello World') # Hello World로 출력, Hello World는 상수



"""예약어(Reserved Words)는 python만이 정한 특별한 의미의 언어이다.
if else whifle ... etc ... """

#Variables : Memory에 사람이 이해할 수 있는 변수명으로 데이터를 넣을 수 있는 공간 확보.

x = 12.2
print(x) # 12.2 가 출력된다.

y = 14
x = 100
print(x) # 100이 출력된다.
print(y)
"""x, y 는 메모리에 할당된 변수의 이름, =은 할당자로 해당변수에 특정 값을 넣어주는
역할을 한다.(일종의 화살표)
그리고 12.2, 14는 해당 변수(x, y)에 우리가 집어넣은 값.
"""

#Assignment Statements(할당문) : 오른 쪽의 표현 결과를 왼쪽의 변수에 저장하는 것

x = 0.6
x = 3.9 * x * (1 - x)
print(x) # 0.936 = 3.9 * 0.6 * (1-0.6) 출력

x = 3.9 * x * (1 - x)
print(x) # 0.2336256 출력. = 3.9 * 0.936 * (1 - 0.936)
