## 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴
# ** 패키지 : 모듈을 모아놓은 것

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date 객체 사용
# import datetime
# day1 = datetime.date(2023, 4, 17)
# day_end = datetime.date(2023, 9 ,18)
# diff = day_end - day1
# print(diff.days)

# 2018년 8월 6일 무슨 요일 일까요?
# weekday() --> 0:월요일 1:화요일 ~~~ 6: 일요일
# import datetime
# day = datetime.date(2018, 8, 6)
# weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
# print(day.weekday()) # 0
# print(weekdays[day.weekday()]) # 월요일

# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년 4일 27일
# 2023-04-27
# 23년 4월 27일
# import datetime
# today = datetime.datetime.today() # today() 는 현재 컴퓨터 시간 가져옴
# print(today) # 2023-04-27 10:50:09.556927, 날짜와 시간 초까지 나옴
# strftime()
# print(today.strftime("%Y년 %m월 %d일")) # 2023년 4월 27일
# %Y 년도 4자리
# %y 년도 2자리
# %m 월
# %d 일
# %H 시간 (24시간)
# %I 시간 (12시간)
# %M 분
# %S 초
# %A 요일
# print(today.strftime("%A")) # Thursday

# time 라이브러리
# 시간 관련
# import time
# time_now = time.time() # 현재 시간 리턴하는 함수
# print(time_now) # 1682560663.8673193 / 1970년 1월 1일부터 현재까지 초단위 시간
# print(time.strftime("%H:%M:%S", time, localtime(time_now)))

# time.sleep()
# 프로그램이 잠시 멈추었다가 다시 시작
# import time
# print("before")
# time.sleep(2)
# print("after") # 비포 출력 후 2초 뒤 에프터 출력함

# for i in range(10):
#     print(i)
#     time.sleep(1.2) # 실수 가능
# # 1.2의 간격으로 0 ~ 9 까지 출력

# 정확하게 n초를 재는 것은 아님. 대략 n초. 유사한 정도.
# 아주 정밀하게 시간을 재는 작업이라면 사용하면 안됨.

# math
# 수학 관련
# import math
# math.ceil() # 올림하는 함수
# result = math.ceil(1.1) # 2, 소수점을 없애면서 앞자리 올려줌
# print(result)
# # math.floor() # 내림하는 함수
# result = math.floor(1.9) # 1, 소수점을 없애면서 앞자리 내려줌
# print(result)
# print(math.pi) # 3.141592653589793

# random
# 난수 관련
import random
# random.random()
# 0.0 ~ 1.0 사이의 실수 중 난수 값
# random_value = random.random()
# print(random_value)

# random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수 값
# 범위가 range와는 다름. 시작 ~ 끝 값 모두 포함.
# random_value = random.randint(1, 10)
# print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
# foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
# food = random.choice(foods)
# print(food) # 무작위로 foods에서 하나 나옴

# random.shuffle()
# 리스트 안에 있는 내용을 임의대로 섞어서 출력
# 리스트 안 data는 바뀌지 않음
# li = [1, 2, 3, 4, 5]
# random.shuffle(li) 
# print(li)

# 로또 자동 번호 추첨
lotto_numbers = list(range(1, 46)) # 범위 1 ~ 45
my_lotto = []
for i in range(6):
    random_value = random.choice(lotto_numbers) # choice 함수는 중복선택 할 수 있음
    if random_value not in my_lotto:
        my_lotto.append(random_value)
print(my_lotto)

# in 연산자
# a in b
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False


# isdigit()
# 숫자로만 이루어진 문자열인지 확인한다.
# 숫자로만 이루어져 있으면 True 아니면 False

# 중복 확인
# duplicate = False
# for i in range(3):
#     if user_input[i] in user_input[i+1:]:
#         duplicate = True
#         break
#     if duplicate:
#         False


# os
# OS 자원을 제어 (os : 운영체제)
# import os
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
# print(os.environ) # 함수가 아니라 변수

# os.getcwd()
# get current working directory
# 현재 작업 공간을 절대경로로 알려줌
# 어디에서 작업하고 있는지 중요함
# print(os.getcwd()) # PS C:\Users\405\my_study>

# os.mkdir(디렉터리)
# 디렉터리(폴더)를 만든다.
# os.mkdir("폴더1")

# os.rename(원래이름, 변경이름)
# 파일의 이름을 바꾼다.
# os.rename("파일1", "파일2")

# os.rmdir(디렉터리)
# 디렉터리(폴더)를 지운다.
# 폴더 안에 아무것도 없어야함 (비어있어야함)
# os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다.
# os.unlink("파일2")

# os.path
# os.path.exists("경로")
# 파일이 있으면 True, 없으면 False
# import os
# if not os.path.exists("없는 파일"):
#     f = open("없는 파일", "w")
#     f.close()
# f = open("없는 파일", "r")
# #else:
# #    print("파일이 없습니다.")

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1개의 경로로 만들어준다.
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트 파일을 작성합니다.")

## 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# PyPI (Python Package Index) 파이썬 소프트웨어 저장 공간 : 오픈소스
# PyPI에 있는 파이썬 패키지를 설치해준다.
# ==> new Terminal 에서 입력 가능

# 패키지 설치 (최신 버전 설치됨)
# pip install 패키지 이름

# 패키지 삭제
# pip uninstall 패키지 이름

# 특정 버전으로 설치 (원하는 버전 명시 가능)
# pip install 패키지 이름 ==1.0.5

# 최신 버전으로 업그레이드
# pip install --upgrade 패키지이름
# ** pip 업그레이드 하는 방법 - 인터넷 검색으로 확인 가능

# 설치된 패키지 리스트 확인
# pip list

# 현재 설치된 패키지들 나옴
# pip freeze


