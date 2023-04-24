# funtion 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다.

# 내장 함수 (built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print( )
# len( )
# zip( )
# int( )
# float( )
# str( )
# list( )
# range( )

# abs( )
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다.
# print(abs(100))
# print(abs(-100))
# print(abs(3.15))
# print(abs(-3.15))

# sum( )
# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
#print(sum([1, 2, 3, 4, 5])) # 15

# max( )
# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) # 5

# min( )
# min(리스트)
# 리스트에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5])) # 1

# chr( )
# chr(정수)
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
#print(chr(65)) # A

# ord( )
# ord(문자)
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
# print(ord("A")) # 65
# chr, ord 세트

# round( )
# round(값, 소수 자릿수)
# 반올림 함수
# print(round(1.234)) # 1
# 숫자만 적었을 땐 소수점 다 버림
# print(round(1.234, 2)) # 1.23
# print(round(1.369, 1)) # 1.4
# 뒤에 숫자 적어주면 숫자 자리 소수점까지 반올림 해줌

# 함수 정의 (define)
# 함수 이름
# 함수 입력값 (parameter)
# 함수 결괏값 (return value)
"""
def 함수이름 (함수입력값):
    함수기능코드
    return 함수 결괏값
"""
# def 
# 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜서 지어야한다.
# 영어, 숫자, _만 사용 가능
# 숫자로 쓰면 안됨
# 띄어쓰기하면 안됨
# 키워드 사용하면 안됨
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋음

# def print_names( ): # 빈칸은 입력값이 없는 함수라는 의미.
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")
# print_names()

# def get_name():
#     return "여지원"

# def print_my_name():
#     print(get_name())
# print_my_name()
# a = print(10) # 리턴이 없음
# b = get_name() # 리턴이 있음
# print(a)
# print(b)

# parameter
# 함수에 입력하는 값
# 괄호 안에 있는 값
# 매개변수, argument 혼용 

def add(a, b):
    return a + b
def print_add(a, b):
    print(a + b)
print_add(1, 2)

result = print_add(1, 2)
print(result)

print_add("안녕", 1) # Error
print_add(1, 2)
print_add("안녕", "하세요")
print_add("하세요", "안녕")
순서 잘 지키기, 순서 안지키면 Error 발생 가능성 있음
print_add(b = "하세요", a = "안녕") # 매개변수에 아예 특정해서 넣어버리면 순서 바뀌어도 상관없음

def swap_number(a, b):
    temp = a
    a = b # 블럭 안에서 적용받는 변수 : 지역변수, local변수
    b = temp
    print(a, b)
    return(a, b)

a = 1 # 전역변수, global변수
b = 2
print("함수 호출 전", a, b)
a, b = swap_number(a, b)
print("함수 호출 후", a, b)
지역변수와 전역변수의 이름이 같더라도 다른 변수임 (주의)

# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

def mul(a, b):
    return a * b

print(mul(2, 6))

result = mul(1, 2)
print(result)

# 기본 값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
# def mul(n1, n2=1):
#     return n1 * n2

# print(mul(1, 2))
# print(mul(1))

# def test_func(x, test=5): # 기본값으로 리스트 사용하지 말 것, 누적되어 재사용됨, 예측하는 결과와 다르게 나옴
#     test = test
#     print(x, test)

# print(test_func(1))
# print(test_func(2))

# def test_func2(x, test=None):
#     if test == None:
#         test = []
#     tset.append(x)
#     print(x, test)

# 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 위치해야함, Erorr 발생
# def sub(n1, n3, n2=0):
#     print(n1 - n2 - n3)

# *를 사용한 매개변수
# 입력값이 몇개가 될 지 모를 때 (안 정해졌을 때)
# def add_many(*args):
    # 튜플처럼 사용
    # 인덱싱, 슬라이싱 사용가능
    # for문 사용가능
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1 = add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)

# def calc_many(n1, *args):
#     result = n1
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용하게 변수를 받아옴
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a = 1, b = 2)
# print_kwargs(name = "이름", age = 10)

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.
# deg tset_func5():
# print(1)
# print(2)
# return None
# print(3)
# print(4)
# print(5)

# 함수의 반환값을 무조건 1개이다.
# def test_func6(a, b):
#     #retrun a + b (a + b, a * b)
#     return a * b, a * b

# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1, 2)
# print(result)
# print(res_add, res_mul)

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True, 짝수면 False

# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
# print(is_odd_number(5))
    
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False
# print(is_odd_number(2))

# def is_odd_number(n):
#     return n % 2 == 1
# print(is_odd_number(5))

# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 테두리와 함께 문자를 출력한다.
# 함수 이름 get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시
"""
*****
hello
*****
"""
# def get_bordered_str(message):
#     message = str(message) # 숫자도 문자형이 될 수 있도록 str 사용
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
#     return None # 생략가능, 반환값을 None으로 명시했기 때문
#get_bordered_str("hello")

# is로 시작하는 함수 이름은 질문형
# bool타입 함수(True, False)를 return하게 됨

#get_bordered_str("12345")
#get_bordered_str(12345)

# 속도를 변환하는 함수
# m/s단위의 속도가 입력되면 km/h단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도

# def convert_velocity(velocity):
#     # 1m/s로 1시간동안 가면 몇m ?
#     # 3600m/h / 1000m(1km)
#     # 1m/s --> 3.6km/h
#     # 1m/s * 3600 / 1000 --> 3.6km/h
#     # 초속 * 3600 / 1000 --> 시속
#     # 초속 * 3.6 = 시속
#     result = velocity * 3.6
#     return result
# velocity = convert_velocity(10)
# print(velocity)

# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None
"""
출력 결과 n -> 4
*
**
***
****
"""

def print_stars(n):
#     for i in range(n): # 0 ~ n-1
#         for j in range(i+1): # 0
#             print("*", end="") # 
#         print()
# print_stars(4)

#     for i in range(0, n+1):
#         print(i * "*")
#     print()
# print_stars(4)

    i = 0
    while i < n:
        j = 0
        while j < i+1:
            print("*", end="")
            j += 1
        print()
        i += 1
print_stars(4)
