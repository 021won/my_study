import numpy as np # Numpy(넘파이) 패키지 임포트
import pandas as pd #pandas(판다스) 패키지 임포트
import matplotlib.pyplot as plt #Matplotlib(맷플롯립) 패키지의 pyplot 모듈을 plt로 임포트
import seaborn as sns #Seaborn(씨본) 패키지 임포트

#경고창 무시
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt # 맷플롯립 import 하기
plt.rcParams['font.family'] = 'NanumBarunGothic' # 나눔바른고딕 적용하기
# 스케일 조정 -> sns.set_context 함수를 이용해 설정이 가능.

sns.set_context('paper', # notebook, talk, poster
                rc={'font.size':15, 
                    'xtick.labelsize':15, 
                    'ytick.labelsize':15, 
                    'axes.labelsize':15})
df_titanic = sns.load_dataset('titanic')    # 타이타닉호 데이터
df_iris = sns.load_dataset('iris')          # 붓꽃 데이터
df_penguins = sns.load_dataset('penguins')  # 펭귄 데이터
df_tips = sns.load_dataset('tips')          # 팁 데이터
df_diamonds = sns.load_dataset('diamonds')  # 다이아몬드 데이터
df_planets = sns.load_dataset('planets')    # 행성 데이터
df_flights = sns.load_dataset('flights')    # 비행 데ㅉ이터

from sklearn.datasets import load_wine      
wine_data = load_wine()
df_wines = pd.DataFrame(data=wine_data.data, # 와인 데이터
                       columns=wine_data.feature_names)
sns.countplot(x='class',hue='who',data=df_titanic)
