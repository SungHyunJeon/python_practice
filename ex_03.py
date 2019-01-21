"""사용자에게 시간(Hours:35시간)과 시급(Rate:2.75달라)을 입력값으로 받아 급여를
계산하는 프로그램을 만들어 보아라. input()함수로 string을 읽어오겠으나
float()을 통해 변환해줘야 한다.
"""


h = input('hours?')
print('hours?', h)
r = input('rate?')
print('rate?',r)

total = float(h) * float(r)
print(total)
