"""
if 조건:
    조건이 True(참)일 때 실행하려는 코드
    코드2줄
    코드3줄
코드4줄
if문은 조건이 True(참)일 때만 안쪽 코드 블럭을 실행
else:
    아닐 때 실행하려는 코드
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1이 True(참)일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일 때 실행
else:
    조건1 False, 조건2 False일 때 실행
"""
# bool

# number1 = 6
# number2 = 6
# if number1 > number2:
#     print(number1 > number2)
#     print("number1이 더 크다.")
# elif number1 == number2:
#     print(number1 == number2)
#     print("같다")
# else:
#     print(number1 > number2)
#     print("number2가 더 크다")

# print(2 > 3) # False
# print(2 >= 3) # False
# print(2 < 3) # True
# print(2 <= 3) # True
# print(2 == 3) # False
# print(2 != 3) # True
# print("a" < "b") # True
# print("CAT" < "DOG") # True
# print("COW" > "CAT") # True
# print("DOG" == "dog") # False
# print("DOG" > "dog") # False

# 논리 연산자 (bool 연산자) (True, False에 적용)
# and   a and b
# a와 b가 모두 True일 때만 True / 아니면 False
# or    a or b
# a와 b 중 하나라도 True면 True / 둘다 False면 False 
# not   not a
# True면 False로 변경, False면 True로 변경
# a, b  피연산자
# and, or, not  연산자
# bool 상수 : True, False

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

# print(not True) # False
# print(not False) # True

# age = 17
# if age >= 20:
#     print("성인입니다.")
# money = 10000
# if money >= 10000:
#     print("부자입니다.")

# age = 17
# money = 10000
# if age >= 20 and money >= 10000:
#     print("성인이고 부자입니다.") # 하나가 False이라 값 출력 안됨
# if age >= 20 or money >= 10000:
#     print("성인 또는 부자입니다.")

if "안녕":
    print("안녕하세요")

if 0:
    print(0)

    
    
    