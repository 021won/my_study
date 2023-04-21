# 변수 이름 규칙
# 영어, 숫자, _ 만 사용 (한글도 가능하나 영어 추천)
# 한글도 되지만 Error 방지로 영어 사용 추천
# 띄어쓰기 불가 _ 로 사용
# 제일 앞에는 숫자가 오면 안됨, 제일 앞에는 영어 또는 _ 가 와야함
# 보통은 영어가 제일 앞에 옴, _ 가 오는 경우는 특별한 상황일 때이며 자주 없음
# 한눈에 무슨 역할하는 변수인지 적는게 생산적임
# 키워드 사용 불가 (오류 방지)
# name = "여지원"
# first_name = "명기"
# last_name = "홍"
# name = last_name + first_name
# print(name) # 위에 name이 있지만 아래로 새로운 name 변수를 주어 값이 변경
a = 6
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)