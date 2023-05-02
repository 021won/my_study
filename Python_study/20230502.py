# # 1번 함수
# def swap_value(x, y):
#     temp = x
#     x = y
#     y = temp

# # 2번 함수
# def swap_offset(offset_x, offset_y):
#     temp = a[offset_x]
#     a[offset_x] = a[offset_y]
#     a[offset_y] = temp

# # 3번 함수
# def swap_reference(list, offset_x, offset_y):
#     temp = list[offset_x]
#     list[offset_x] = list[offset_y]
#     list[offset_y] = temp

# # 테스트
# a = [1, 2, 3, 4, 5]
# swap_value(a[1], a[2])
# print(a) # [1, 2, 3, 4, 5] swap 발생 안함

# swap_offset(1, 2)
# print(a) # [1, 3, 2, 4, 5] swap 발생

# swap_reference(a, 1, 2)
# print(a) # [1, 2, 3, 4, 5] 

# 함수를 만들어보자.
# 이 함수는 두개의 숫자를 input으로 받으면 작은 수로 큰 수를 나눈 몫과 나머지를 반환하는 함수.
# 반환 값은 튜플로 되어 있으며 몫, 나머지 순으로 되어 있다.
# 단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은 수가 0이라면
# 화면에 "0은 사용할 수 없습니다."를 출력하고 종료되어야한다.

# a = int(input("숫자를 입력하세요."))
# b = int(input("숫자를 입력하세요."))

# 다시 확인하기
# def div2(a, b):
#     if a >= b:
#         a // b, a % b
#     elif b > a:
#         pass
#     if a == 0 or b == 0:
#         print("0은 사용할 수 없습니다.")
#     elif a < 0 or b < 0:
#         print("정수를 입력하세요.")
# div2(4, 2)

# def div3(a, b):
#     if a < b:
#         big = b
#         samll = a
#     elif b <= a:
#         big = a
#         small = b
#     if small == 0:
#         print("0은 사용할 수 없습니다.")
#     elif abs(big) < 0 or abs(small) < 0:
#         print("정수를 입력해주세요")
#     else:
#         q = big // small
#         r = big % small
#         return(q, r)

# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수
# 끊는 단위는 따로 정하지 않으며 2로 설정해보자

# def func(string, unit = 2):
#     i = 0
#     while i < len(string):
#         print(string[i : i+unit])
#         i += unit
# func("테스트문장입니다.") 

# def test (*args):
#     print(args)

# def test(*a):
#     print(*a)

# test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# test([1, 2], 3)
# test( [1, 2])

# def test2(**kwargs):
#     print(kwargs)

# test2(a = 1, b = 2, c = 3)

# add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# def add_all(*inputs):
#     s = 0
#     for i in range(len(inputs)):
#         s += inputs[i]
#     return s
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# 여기는 동네 유명한 빵집이다.
# 사람들에게 먼저 온 순서대로 번호표를 나누어주려고 한다.
# 번호표를 나누어주는 함수를 작성해보자.
# 함수는 사람이름으로 되어 있는 리스트를 받아서
# "대기번호 x번 : 사람이름"을 화면에 출력하고 (번호표, 사람이름)을 원소로 이루어진 리스트를 반환한다.

# people = ["펭수", "뽀로로", "뚝딱이", "텔레토비"]

# def func1(line):
#     new_lines = []
#     i = 1 # 대기번호를 트래킹하는 변수 i
#     for x in line:
#         print("대기번호 %d번 : %s" % ((i, x)))
#         new_lines.append(i, x)
#         i += 1 # 별도로 업데이트를 해줘야 함
#     return new_lines

# def func1(line):
#     new_lines = []
#     for idx, val in enumerate(line):
#         print("대기번호 %d번 : %s" % (idx, val))
#         new_lines.append((idx + 1, val))
        
#     return new_lines
# print(func1("펭수"))

# enumerate (열거하다)
# 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수.
# lst = ['a', 'b', 'c']
# for x in enumerate(lst):
#     print(x)

# lst1 = 'abcd'
# for x in enumerate(lst1):
#     print(x)

# zip
# 반복가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수.
# 각 원소들을 튜플의 형식으로 묶어줌.

# str_list = ['one,', 'two', 'three', 'four']
# num_list = [1, 2, 3, 4]

# for i in zip(num_list, str_list):
#     print(i)

# lambda : 한 줄을 실행한 결과 값이 바로 반환값이 됨.

# map : 리스트, 튜플, 스트링 등 자료형 각각의 원소에 동일한 함수를 적용
# items = [1, 2, 3, 4, 5]

# squared = []
# for i in items:
#     squared.append(i * i)

# print(squared)

# squared_map = list(map(lambda x : x ** 2, items))
# print(squared_map)

#lambda와 map을 이용하여 items의 요소들을 string(문자)로 바꾸는 것을 짜봅시다.

# items = [1, 24, 3, 6, 7]
# str_items = list(map(lambda x : str(x), items))
# print(str_items) # ['1', '24', '3', '6', '7']

# list comprehension
# 1.
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #2.
# list_2 = []
# for x in range(10):
#     list_2.append(x)
# print(list_2)

# lc_1 = [x for x in range(10)]
# print(lc_1)

# 10 부터 20 까지의 숫자들 중에서 짝수만을 담은 리스트를 만들어보자!

# list3 = []
# for x in range(10, 21):
#     if x % 2 == 0:
#         list3.append(x)
# print(list3)

# ic_2 = [x for x in range(10, 21) if x % 2 == 0]
# print(ic_2)

# 1부터 10의 제곱수 중, 50 이하인 수만 리스트에 저장하라.
# lc_3 = [x ** 2 for x in range(1, 11) if x ** 2 <= 50]
# print(lc_3) # [1, 4, 9, 16, 25, 36, 49]

# 1부터 10까지의 숫자들 중 홀수 이면 어떤 제곱수를,
# 짝수이면 세제곱수를 담은 리스트를 만들어보자.
# list_4 = []
# for x in range(1, 11):
#     if x % 2 == 1:
#         list_4.append(x ** 2)
#     else:
#         list_4.append(x ** 3)

# print(list_4) # [1, 8, 9, 64, 25, 216, 49, 512, 81, 1000]

# # lc(list comprehension) 사용 시 if 함수가 두개 이상이면 for문 앞으로 들어가야함! 주의!
# lc_4 = [x ** 2 if x % 2 == 1 else x ** 3 for x in range(1, 11)]
# print(lc_4) # [1, 8, 9, 64, 25, 216, 49, 512, 81, 1000]

# for문 + for문

# word1 = 'hello'
# word2 = 'world'

# result = [i + j for i in word1 for j in word2]
# print(result)

# for i in word1:
#     for j in word2:
#         result = [i + j]
#         print(result)

# for문 + if문
# 40이하의 숫자는 5를 더하고, 40 초과의 숫자는 41로 바꾸어
# 리스트로 저장하고, 리스트를 출력하라.

# list_5 = [12,67,32,48,19,57,29,49]
# for i in list_5:
#     if i <= 40:
#         i + 5
#     else:
#         i = 41
#     print([i])

# lc_5 = [i + 5 if i <= 40 else 41 for i in list_5]
# print(lc_5)


# improt numpy as np

# n = 1000000
# numpy_arr = np.arange(n)
# python_list = list(range(n))

# import time
# start = time.time() # 시작시간 저장
# python_list = [x ** 3 + 10 for x in python_list]
# print('time:', time.time()-start) # 현재시각 - 실행시각 = 실행시간

# A = [1, 2, 3, 4]
# a = np.array(A, np, int)
# print(type(a))
# print(a)

# 벡터화
# 배열은 for문을 작성하지 않고 데이터를 일괄 처리하는 것

# 브로드캐스팅
# 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy의 기능.

# dtype
# 배열에 담긴 원소의 자료형 (ndarray는 같은 자료형을 담음.)

# size
# 배열에 있는 원소의 전체 갯수

# ndim
# 배열의 차원의 갯수

# # 0차원 (상수)

# import numpy as np
# a = np.array(10)
# print(a)
# print(a.ndim)

# # 1차원

# a = np.array([1, 2, 3])
# print(a)
# print(a.ndim)

# # 2차원

# a = np.array([[1, 2], [3, 4]])
# print(a)
# print(a.ndim)

# # 3차원

# a = np.array([[[1, 2], [3, 4]]])
# print(a)
# print(a.ndim)
# print(a.shape)

# range 함수를 이용

# import numpy as np

# arr1 = np.array(range(20))
# print(arr1)

# arr2 = np.arange(20)
# print(arr2)

# zeros
# 0, 공간이 있음, 0이 할당됨

# arr3 = np.empty((2, 3), dtype = np.float32)
# print(arr3)
#[[0.0000000e+00 7.1746481e-43 1.4349296e-42]
# [2.4035071e-41 2.7963191e-39 1.1387602e-38]]
# 실수, 공간 없음, 0보다 더 아래

# 배열 결합 함수
# hstack, concatenate(axis=0)
# 두 배열을 왼쪽에서 오른쪽으로 붙이기

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.hstack([a, b])) # 옆으로 나열
# print(np.concatenate((a,b),axis=0))
# print(np.vstack([a, b])) # 아래로 나열
# [[1 2 3]
#  [4 5 6]]
# print(np.concatenate((a,b),axis=1)) # 1Dvector는 안됨

# c = np.array([[0,1,2], [3,4,5]])
# d = np.array([[6,7,8], [9,10,11]])

# print(np.concatenate((c, d), axis = 1))
# [[ 0  1  2  6  7  8]
#  [ 3  4  5  9 10 11]]

# 두 배열을 위 아래로 붙이기
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.column_stack([a, b]))
# [[1 4]
#  [2 5]
#  [3 6]]



# seed
# 난수 초기값 부여 -> 재현 가능성 (Reporducibility)
# 내가 다른 사람에게 코드를 보냈을 때 그대로 나오게 함

# np.random.seed(42)
import random

# lotto_numbers = list(range(1, 46))
# my_lotto = []
# for i in range(6):
#     random_value = random.choice(lotto_numbers)
#     if random_value not in my_lotto:
#         my_lotto.append(random_value)
# print(my_lotto)


import numpy as np


def make_lotto(count):
    for i in range(count):
        lotto_num = [] # 로또 번호가 담길 리스트형 변수
        for j in range(6): # 6번 반복
            lotto_num = np.random.choice(range(1, 46), 6, replace = False)
            lotto_num.sort() # 값 정렬
        print('{}.로또번호: {}').format(i + 1, lotto_num)

count = int(input('로또 번호를 몇개 생성할까요?'))
make_lotto(count)