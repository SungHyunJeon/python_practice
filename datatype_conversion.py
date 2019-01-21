#타입 변환 python에는 타입을 변환할 수 있는 함수가 내재돼 있기에 간단히 변환 가능하다.
#변환하고자 하는 타입 형식으로 감싸주면 타입 변환 가능.

"""예를 들어, i라는 variable을 integer type으로 선언했을 때
만약 i variable을 부동 소수점 수 타입으로 바꾸려면 f = float(i)로 입력
"""

i = 42
type(i) # int type
f = float(i) #float type으로 conversion
print(f) # 42.0으로 출력
type(f) # float type


sval = '123'
type(sval) # string type
print(sval + 1) # string type과 int type을 연산했으니 오류

ival = int(sval)
type(ival) # int type
print(ival + 1) # int type 간의 연산이니 124로 출력됨.
