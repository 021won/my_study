# for문
"""
for 변수 in iterable값:
    반복할 코드
"""
# li_1 = ["one", "two", "three"]
# for i in li_1:
#     print(i)
# 첫번째 요소부터 마지막 요소까지 변수에 대입하면서 반복
# s1 = "Hello"
# for i in s1:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)
# numbers.reverse()
# for number in numbers:
#     print(number)

# range()
# 숫자 range객채를 만들어주는 함수
# range(끝 정수)
# 0 ~ 끝 정수 - 1
# for i in range(10):
#     print(i) # 0 ~ 9까지 출력
# range(시작, 끝)
# 시작 ~ 끝 - 1
# for i in range(1,11):
#     print(i) # 1 ~ 10까지 출력
# range(시작, 끝, 스텝)
# 시작 ~ 끝 - 1 까지인데 스텝만큼 차이나게
# for i in range(1, 21, 2):
#     print(i) # 1 ~ 19까지 출력되며 2씩 차이나게 출력

# for문을 사용하여 2부터 30까지 출력해보세요
# for i in range(2, 31):
#     print(i)
# # for문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해보세요
# for i in range(2, 31, 2):
#     print(i)

# for i in range(2, 31):
#     if i % 2 == 1: # 홀수
#         pass # 아무것도 안하고 그냥 넘어갈 때
#     else: # 짝수
#         print(i)

# for i in range(2, 31):
#     if i % 2 == 0: # 짝수
#         print(i)

# for문을 사용하여 10부터 1까지 출력해보세요
# for i in range(10, 0, -1):
#     print(i)

# for i in reversed(range(1, 11)):
#     print(i)

# for i in range(1, 11)[::-1]: # 슬라이싱 [시작인덱스 : 끝인덱스 : 방향]
#     print(i)

# money = 2000
# price = 1000
# coffee = 5
# for i in range(coffee): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :", coffee - 1 -i) # 4 ~ 0
#     if money < price:
#         break

# for i in range(1, coffee + 1): # 1 ~ 5
#     print("남은 커피 :", coffee - i) # 4 ~ 0

# for i in range(coffee):
#     coffee -= 1
#     print("남은 커피 :", coffee) # 4 ~ 0

# prices = [500, 700, 930]
# money = int(input("돈:"))
# for i in range(len(prices)): # len 길이, 개수 : 3
#     price = prices[i]
#     print(money // price)
#     print(money % price)

# for price in prices:
#     print(money // price)
#     print(money % price)

# scores = []
# for i in range(5):
#     score = int(input("시험점수 : "))
#     scores.append(score)
    
# for i in range(1, 10): # 1 ~ 9
#     print("2 *", i, "=", 2*i)

# 이중 for문
# for i in range(2, 10): # 2 ~ 9
#     print(i, "단")
#     for j in range(1, 10): # 1 ~ 9
#         print(i, "*", j, "=", i*j)
#     print("---------")
