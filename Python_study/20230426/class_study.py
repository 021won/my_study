# 객체지향(oop, object oriented programing)
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출
# 캡슐화 : 데이터의 구조와 연산을 결합
# 상속 : 상위 개념의 특징이 하위 개념에 전달
# 다형성 : 유사 객체의 사용성을 그대로 유지

# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다.

# 클래스는 객체를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성) : 객체가 가지고 있는 변수
# 메소드 : 객체가 가지고 있는 함수(멤버 함수)
"""
class 클래스 이름:
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 지켜야 함
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# 단어 구분될 때 대문자
# class Car:
#     def move(self): # 클래스가 가지고 있는 함수, 클래스 내부에 있는 함수, 메소드(멤버 함수)
#         print("move")

# class SportsCar:
#     pass

# 인스턴스
# 클래스를 통해 생성된 객체
# my_car = Car()
# my_car.move()
# . ---> 객체 멤버 접근 연산자
# li = [1,2,3,4,5]
# li.append(6)

# 파이썬에서는 모든게 객체다
# 내장함수 type()
# 데이터의 자료형을 반환한다.
# 어떤 종류의 객체인지 확인해주는 함수
#

# str(문자열) 메소드
# upper()
# 모두 대문자로 변경
# s = "Hello"
# print(s.upper())

# "Hello".upper # . 넣어 사용가능

# lower()
# 모두 소문자로 변경
# s = "Hello"
#print(s.lower())

# strip()
# 문자열 양쪽 끝의 특정 문자를 제거
# s1 = "          Hello            "
# print(s1.strip())
# lstrip(), rstrip()
# 왼쪽, 오른쪽 끝의 특정 문자 제거
# print(s1. lstrip())
# print(s1.rstrip())

# split()
# 구분자로 분할하여 리스트로 반환
# s2 = "Hello, World, Python"
# print(s2.split(','))

# replace()
# 문자열의 특정 부분을 대체
# print(s2.replace(',', ' '))
# s2 = s2.replace(',', '-')
# print(s2)
# 수정이 안되는 immutable str을 재할당하기 위한 함수
"""
"Hello" --> "hello"
"""
# s3 = "Hello"
# s3[0] = h # 인덱싱으로 변경하려고 하면 Error
# print(s3.lower())
# print(s3.replace('H', 'h'))
# 수정불가이기 때문에 변경한 것이 아니라 재할당 한 것.

# self 매개변수
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용
# class Person:
#     def say(self):
#         self.name = '사람1'

#     def move(self):
#         pass

#     def eat(self, food): # food도 쓰고 싶으면 self 다음으로 적으면 됨, self는 첫번째 매개변수이기 때문.
#         self.sleep()
#         print(f"{self.name}이 {food}를 먹었습니다.")
    
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.") # 객체 자신을 참조하여 클래스에 정의된 멤버에 접근함.

# person1 = Person()
# person1.say() # Hello
# person1.eat("밥") # 밥을 먹었습니다.
# self는 호출에는 사용되지 않아 값을 주지 않음, self는 person1 이다.

# initializer 초기자, 초기화기
# initialize가 발생할 때 어떤 일을 하는 지
# initialize 초기화 
# 시작한다는 의미, 만든다라는 의미와 유사.
# refresh : 0으로 만들어버린다. 와는 다른 의미
class Person:
    def __init__(self, name, age, gender, phone): # initialize 호출 시 약속한 코드
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        print("initialize")

# Person 클래스에 introduce 메소드를 추가
# 이름, 나이, 성별을 print하는 메소드

    def say_name(self):
        print(self.name)

    def introduce(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")
        print(f"나이는 {self.age}살이고, 성별은 {self.gender}입니다.")
        print(self.name, self.age, self.gender)

print("before")
person2 = Person("이름", "20", "남자", "010-1234-5678")
print("after")

person2.say_name()
person2.introduce()
        
# 상속 inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name}이 생성되었습니다.")

#     def say(self):
#         print("")



# class Dog(Animal): # 부모클래스에 정의가 되어있기 때문에 메소드 그대로 물려받아 사용할 수 있음.
#     def say(self):
#         print("멍멍")
#     # 메소드 재정의
#     # method overriding

# my_dog = Dog("백구")
# my_dog.say()

# class Cat(Animal):
#     def say(self):
#         print("야옹")

# my_cat = Cat("나비")
# my_cat.say()

# 이름, 나이, 학교, 학년을 멤버변수로 저장하는 메소드를 만드세요.
class Student:
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

# 이름, 나이, 학교, 학년을 print 하는 메소드를 정의하세요.
    def introduce(self):
        print(f"{self.name}, {self.age}, {self.school}, {self.grade}")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()
