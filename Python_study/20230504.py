# Pandas

# 결측치 (missing value)
# stock.isnull().sum()

# 데이터의 자료형 -> info()

# unique
# 중복되는 값을 제거하고 유일한 값만 담고 있는 Series를 반환.

# map 함수
# Series의 각각의 element들을 다른 어떤 값을 대체하는 역할.

# apply
# map보다 적용할 수 있는 범위가 큰 것.
# 반복되지 않아서 (10)이라고만 하면 안되고 (10,) 컴마를 찍어줘야함 (?)

# applymap
# 모든 원소에 원소별로 함수에 적용.

# concat
# 데이터 병함

# s1 = pd.Series([100, 200], index = ['c', 'd'])
# s2 = pd.Series([300, 300, 300], index = ['c', 'd', 'e'])
# s3 = pd.Series([500, 600], index = ['f', 'g'])

# print(s1, s2, s3, sep='\n\n')

# Matplotlib
# 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.02)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label='sin', color = (0.1, 0.3, 0.5)) #RGB
plt.plot(x,y2,label='cos', color = '#f6a2fc') # hex color
plt.legend()
plt.show()
