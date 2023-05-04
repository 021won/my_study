# import random

# true_value = random.randint(1, 100)
# input_value = 99999 # 임의의 값 할당.
# print("숫자를 맞춰보세요.")

# while true_value != input_value:
#     input_value = int(input())
#     if input_value > true_value: # 사용자의 입력값이 true_value 보다 클 때
#         print("숫자가 너무 큽니다.")
#     else:
#         print("숫자가 너무 작습니다.") # 사용자의 입력값이 true_value 보다 작을 때
# print(f"정답입니다. 입력한 숫자는 {true_value}입니다.")

# word = ["school", "game", "piano", "science", "hotel", "mountain"] 중
# 글자수가 6글자 이상인 문자를 모아 새로운 리스트를 생성하세요.

word = ["school", "game", "piano", "science", "hotel", "mountain"]
a = list()
for i in range(len(word)):
    if len(word[i]) >= 6:
        a.append(word[i])
print(a) # ['school', 'science', 'mountain']

# 1-100 까지 숫자 중
# 3과 5의 공배수일 경우 "3과 5의 공배수"
# 나머지 숫자 중 3의 배수일 경우 "3의 배수"
# 나머지 숫자 중 5의 배수일 경우 "5의 배수"
# 모두 해당되지 않을 경우 그냥 숫자를 출력하세요.

a = int(input("정수를 입력하세요."))
if a <= 0:
    print("음수는 정의하지 않음.")
else:
    for i in range(1, a+1):
        if i % 3 == 0 and i % 5 == 0:
            print("3과 5의 공배수")
        elif i % 3 == 0:
            print("3의 배수")
        elif i % 5 == 0:
            print("5의 배수")
        elif 1 <= i <= 100:
            print(i)
        else:
            print("1과 100 사이의 숫자가 아닙니다.")

# 사용자로부터 숫자를 계속 입력받다가 s or S 를 입력하면 합계 출력

c = 0
d = 1

while (d == 1):
    a = (input("입력하시오."))
    if (a == "s" or a == "S"):
        d =0
    else:
        a = int(a)
        c += a
print(c)        

# 사람별 평균 구하기.

kor_score = [39, 69, 20, 100, 80]
math_score = [32, 59, 85, 30, 90]
eng_score = [49, 70, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score: # kor, math, eng 과목 선택
    for score in subject: # 과목 선택 후
        student_score[i] += score # 각 학생마다 개별로 교과 점수를 저장
        # print(subject, score, "i:", i, student_score) # kor -> math -> eng
        i += 1 # 학생 index 구분
    i = 0 # 과목이 바뀔 때 학생 인덱스
else:
    a, b, c, d, e = student_score # 학생별 점수를 unpacking
    student_average = [a / 3, b / 3, c / 3, d / 3, e / 3]
    print(student_average) # [40.0, 66.0, 51.0, 63.333333333333336, 90.0]