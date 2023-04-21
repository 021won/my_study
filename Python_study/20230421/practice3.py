# 2 ~ 9사이의 숫자를 입력받아 해당하는 단의 구구단을 출력하세요
# i = int(input("구구단 몇 단?"))
# if 2 <= i <= 9: 
#         input("잘못 입력되었습니다. 다시 입력하세요.")
# if i in range(2, 10):
#     print(i, "단")
#     for j in range(1, 10):
#          print(i, "*", j, "=", i*j)

# n = range(2, 10)
# if 2 <= n <= 9: # 2 ~ 9 사이의 숫자라면
      
    #   pass
# n = int(input("구구단 몇 단?"))
# while not 2 <= n <= 9: # if 2 <= n <= 9: # 2 ~ 9 사이의 숫자 / not으로 참 거짓 변경
#       print("2 ~ 9 사이의 숫자를 입력해주세요.")
#       n = int(input("구구단 몇 단?"))
# for i in range(1, 10):
#       print(n, "*", i, "=", n*i)

# 정수를 입력받고 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하세요.

# n = int(input("정수 : "))
# i = 1
# while True:
#     if i ** 2 > n:
#         break
#     answer = i ** 2
#     i += 1
# print(answer)

# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요

# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]
# for i in range(5):
#     print(li_1[i] + li_2[i] + li_3[i])
    
# zip 함수
# 길이가 같은 list를 묶어서 for문 등으로 사용가능한 iterable
# zip( )
# for x, y, z in zip(li_1, li_2, li_3):
#    print(x + y + z)


# while i < 5:
#     print(li_1[i] + li_2[i] + li_3[i])
#     i += 1

# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
# 단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝 이라고 출력하세요.

# n = int(input("정수 : "))
# for i in range(1, n + 1):
#     # 3, 6, 9가 들어있으면
#     answer = i
#     for j in str(i):
#          if int(j) % 3 == 0 and j != "0":
#             answer = "짝"
#             break
#     print(answer)


# 정수를 입력받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수

n = int(input("정수 : "))
# for i in range(1, n + 1): # 1 ~ n
#     if n % i == 0:
#         print(i)
    
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1