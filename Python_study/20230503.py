# add_all 함수를 짜봅시다.
# add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# def add_all(*input):
#     s = 0
#     for i in range(len(inputs)):
#         s += inputs[i]
#         return

# numpy 
# ndarray vs.list
# 연속된 메모리 블록에 데이터를 저장
# 같은 종류의 데이터를 담음
# 값만 복사하기 때문에 리스트 형태로 가져옴

# Ndarray 타입을 검색하거나 슬라이싱은 참조만 할당하므로 변경을 방지하기 위해서는 새로운 ndarray로 만들어 사용 .copy 메소다가 필요.

# ndarray

# import numpy as np
# print(np.__version__)

# A = [1, 2, 3, 4]

# a = np.array(A, np.int) # 버전이 높아져서 np.int는 안적어도 된다고 함
# print(type(a))
# print(a)

# A = [1, 2, 3, 4]
# a = np.array(A)
# s = a[:2]
# d = np.asarray(s)

# print('A의 출력입니다. %a' % a)
# print('s의 출력입니다. %a' % s)

# ss = a[:2].copy()
# print(ss.size)
# ss[0] = 99
# print(a)
# print(type(a))

# 벡터화

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# arr = np.zeros((3, 2))
# print(arr)

# arr.flatten() # 1D vector로 만드는 것.
# arr = np.array([[1, 2],[3, 4]])
# arr.flatten()
# print(arr)

# reshape
# 이미 존재하는 배열을 내가 원하는대로 shape을 조정 함.
# arr = np.arange(12)
# arr.reshape(3, 4)
# arr.reshape(1, 12) # = flatten()
# arr.reshape(12, 1)
# arr.reshape(2, 6)
# arr.reshape(6, 2)

# arr = np.arange(20)
# arr.reshape(4, 5)
# print(arr)

# arr = np.arange(20).reshape(4,5)
# print(arr)

# print(arr.transpose().shape)
# arr.transpose()

# arr1 = np.arange(4),reshape(-1, 2)
# print(arr1)


# .sort : raturn 값이 있음
# .sortde : return 값이 없음

# x = np.arange(6).reshape(-1,3)
# print(x)

# T operation
# x.T
# print(x)

# 0 ~ 20까지의 숫자를 배열을 만든 다음에 arr1에느 짝수 arr2는 홀수가 들어간 배열을 출력해보자.


# 브로드 캐스팅
#lst = list(range(6))
# print(lst)

# view

# arr2d = np.arange(20).reshape(4,-1)
# arr2d[0] # 첫번째 행
# arr2d[1][2] # 재귀적 접근 / 1행 2열
# arr2d[1, 2] # 컴마를 이용하여 쉽게 인덱싱을 할 수 있음
# arr2d[:3][:2] # 행과 열을 접근하기 위해서는 컴마로 연결해야 함

# 불리안 배열
# arr = np.array([0, 1, 2, 3, 4])
# print(arr[[True, False, True, False, True]])

# arr2d = np.arange(20).reshape(4,5)
# print(arr2d[[0,2]]) # 0행과 2행 # multi index는 [] 하나 더 추가해야함

# 유니버설 함수
# arr = np.arange(-3,3).reshape(3,-1)
# print(arr)
# np.exp(arr)

# floor : 소수점 버리기
# np.floor(arr)

#이항 유니버설 함수
# arr1 = np.arange(8).reshape(2,-1)
# arr2 = np.arange(-40,40,10).reshape(2,-1)
# print(arr1)
# print(arr2)

# np.maximum(arr1,arr2)
# 같은 원소에서 가장 큰 값

# np.subtract(arr1,arr2)
# 뺄셈

# np.multiplay(arr1,arr2)
# 같은 원소끼리 곱셈

# 통계 메서드
# arr = np.arange(4).reshape(2,2)
# print(arr.sum())
# print(arr.sum(axis = 0))
# print(arr.sum(axis = 1))

# print(arr.mean())
# print(arr.mean(axis = 0))
# print(arr.mean(axis = 1))

# where
# x if 조건 ease y의 벡터화 버전
# munpy를 사용하여 배열을 빠르게 처리 할 수 있으며, 다차원도 간결하게 표현이 가능

# xarr = np.array([100,200,300,400])
# yarr = np.array([1,2,3,4])
# cond = np.array([True,False,True,False])
# print(np.where(xarr>200,max(xarr),0))
# print(np.where(xarr % 3 ==0,1,0))

# sort()
# np.random.seed(42)
# arr = np.randem.randint(1,100,size=10) # 1~100까지의 정수 중에 10개를 뽑아주세요

# -np.sort(-arr) # 부호를 이용하여 내림차순으로 정렬
# array의 sort에서는 내림차순, 오름차순을 선책하는 옵션이 없다.

# lst = [1, 32, 4, 1, 20]
# print(lst.sort(reverse = True))

# 선형대수 패키지

# 단위행렬
# 대각 원소 1이고, 나머지는 0인 n차 정방행렬을 말하며, numpy의 eye()함수를 사용하여 만들 수 있음
# import numpy as np
# identity = np.eye(4)
# identity = np.eye(2,3)
# print(identity)

# 대각행렬
# 대각 성분 이외의 모든 성분이 모두 '0'인 n차 정방행렬을 말함

# x = np.arange(9).reshape(3,-1)
# print(x)
# print(np.diag(x)) # diagonal matrix
# print(np.diag(np.diag(x)))

# dot
# 원소간의 곱 (element-wise product)
# 벡터의 내적. (행렬의 곱)
# a = np.arange(4).reshape(-1,2)
# print(a)
# a * a = dot product
# print(np.multiply(a,a))
# print(np.dot(a,a)) # 행렬의 곱

# matmul : matrix multuplication
# a = np.random.randint(-3,3,10).reshape(2,5)
# b = np.random.randint(0,5,15).reshape(5,3)
# print(a.shape,b.shape)

# ab = np.matmul(a,b)
# print(ab.shape,'\n') # \n : 개행
# print(ab)

# ba = np.matmul(b,a)
# ab =np.matmul(a,b.T)
# print(ab)
