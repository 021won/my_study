# while 반복문
"""
while 조건:
    반복할 코드
"""
# 조건이 참인 경우에 코드를 계속 반복
# Flase일 경우 반복하지 않음
# n = 1
# while n <= 1000:
#     print(n)
#     n += 1 # n = n + 1

# s1 = "안녕"
# s1 += "하세요"
# print(s1)

# while 반복문을 활용하여 10부터 1까지 순서대로 출력하세요.
# n = 10
# while n >= 1: # n > 0
#     print(n)
#     n -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price:
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은 커피:", coffee)
#     if coffee == 0:
#         break 

# break
# 반복문을 즉시 종료한다.

# while 반복문을 활용하여 1부터 10까지 홀수만 출력한다.
# a = 1
# while a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1

# continue
# 반복문의 제일 처음으로 돌아감
# b = 0
# while b <= 9:
#     if b % 2 == 0:
#         b += 1
#         continue
#     print(b)
#     b += 1

# while True:
#     print("hi")

# while True:
#     users_input = input("종료하려면 1을 입력해주세요")
#     if users_input == "1":
#         break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 (a + b)

# while True:
#     print("""
#     계산기
#     ======
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input("계산을 선택하세요 : ")
#     if operator == "1":
#         print("1 + 2 =", 1 + 2)
    
#     if operator == "2":
#         print("1 - 2 =", 1 - 2)

#     if operator == "3":
#         print("1 * 2 =", 1 * 2)

#     if operator == "4":4
#         print("1 / 2 = ", 1 / 2)
    
# 코드를 수정해서 사용가자 입력한 숫자를 계산하도록 변경하시오.
# "q"를 누르면 종료되도록 변경하시오.
# while True:
#     print("""
#     계산기
#     ======
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input("계산을 선택하세요. : ")
#     a = int(input("숫자 1을 입력하세요. : "))
#     b = int(input("숫자 2를 입력하세요. : "))
#     if operator == "1":
#         print(a, "+", b, "=", a + b)
    
#     elif operator == "2":
#         print(a, "-", b, "=", a - b)

#     elif operator == "3":
#         print(a, "*", b, "=", a * b)

#     elif operator == "4":
#         print(a, "/", b, "=", a / b)

#     elif operator == "q":
#         break
        
# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개 수와 잔돈을 출력한다.
# 커피는 500원, 음료수는 700원, 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈 :"))
# while idx < len(prices):
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1

# while 반복문을 사용해서 scores 리스트에 시험 점수 5개를 정수형으로 입력받으세요.

# scores = []
# n = 0
# while n <5:
#     score = int(input("시험점수 :"))
#     scores.append(score)
#     n += 1
# print(scores)

# while 반복문을 사용하여 구구단 2단을 출력하세요.

n = 1
while n < 10:
    print("2 *", n, "=", 2*n)
    n += 1