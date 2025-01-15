# 함수
# 수학의 함수와 동일

print('함수!!') # 내장(built-in)함수

# 함수 정의(definition)
# 사용자 정의함수
def add(a, b):
    result = a + b
    return result # return -> 결과를 돌려줘(반환하라!)

def minus(a, b):
    result = a - b
    return result

def multi(a, b):
    result = a * b
    print('곱의 결과는', result) # 300 결과가 나옴
    #return # 아무값도 반활할 게 없으면 리턴은 생략함

def divide():
    result = 100 / 4
    print('나누기의 결과는', result)

# def는 정의 아래가 수식

x = 11
y = 22
z = add(x, y)
print('합의 결과는', z)

x = 101
y = 203
print('합의 결과는', add(x, y))

x = 35
y = 15
print('차의 결과는', minus(x, y))

x = 30
y = 10
multi(x, y)

x = 100
y = 5
divide()

''' 내장함수 - 파이썬에서 자주 사용할 것 같은 함수를 미리 만들어둔것 '''
# 대부분(standard library)에 들어있음
print(max(1,3,7,15)) # max == 최대값
print(min(1,3,7,15)) # min == 최저값
print(abs(-5)) # abs == 절대값
print(2 ** 10)
print(pow(2, 10)) # == 2 ** 10