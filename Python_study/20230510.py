import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

# 당뇨병 예측하기

# age : 나이
# sex : 성별
# bmi : 체질량지수
# bp : 평균 혈압
# s1 : 혈중 총 콜레스테롤
# s2 : 저밀도 지질단백질
# s3 : 고밀도 지질단백질
# s4 : 총 콜레스테롤 수치
# s5 : 혈중 트리글리세라이드 수치
# s6 : 혈당 수치

#diabetes = load_diabetes()
# print(diabetes)
# print(diabetes.data.shape, diabetes.target.shape)
# print(dir(diabetes))
# print(type(diabetes))
# print(diabetes.DESCR)
# input data 보기
# print(diabetes.data[0:3])
# output data 보기
# print(diabetes.target[0:3])
# print(diabetes['feature_names'])

# 당뇨병 환자 데이터 시각화 하기

# plt.scatter(diabetes.data[:, 2], diabetes.target)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# df = pd.DataFrame(diabetes.data, columns = diabetes['feature_names'])
# df['target'] = diabetes.target
# print(df.head())
# print(df.describe())
# print(df.info())
# print(df.isna().sum())
# sns.pairplot(df[["target", "bmi", "bp", "s1"]])
# plt.show()
# df_corr = df.corr()
# print(df_corr)
# cor_order = df_corr.loc[:'s6', 'target'].abs().sort_values(ascending = False)
# print(cor_order)

# 상관계수가 0.5를 넘은 bmi와 s5를 대상으로 산점도와 회귀선을 그려보자.

# names = ['target', 'bmi', 's5']
# diabetes_df = df.loc[:, names]

# plt.figure(figsize = (16, 6))
# for i, name in enumerate(names[1:]):
#     ax = plt.subplot(1, 2, i + 1)
#     sns.regplot(x = name, y= names[0], data = diabetes_df, ax = ax)
# plt.show()
# from sklearn.model_selection import train_test_split

# x_data = diabetes_df.loc[:, ['bmi', 's5']]
# y_data = diabetes_df.loc[:, 'target']

# X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.2, random_state = 1)
# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# from sklearn.linear_model import LinearRegression

# lr = LinearRegression()
# lr.fit(X_train, y_train)
# lr.score(X_train, y_train)

# print(np.round(lr.coef_, 2))
# print(np.round(lr.intercept_, 2))

# pred = lr.predict(X_test)
# print(pred)

# bmi prediction

# plt.figure(figsize = (10, 6))
# plt.scatter(X_test['bmi'], y_test, label = 'test')
# plt.scatter(X_test['bmi'], pred, c = 'r', label = 'predict')
# plt.legend()
# plt.show()

# s5 prediction
# plt.figure(figsize = (10, 6))
# plt.scatter(X_test['s5'], y_test, label = 'test')
# plt.scatter(X_test['s5'], pred, c = 'r', label = 'predict')
# plt.legend()
# plt.show()

# from sklearn.metrics import mean_squared_error
# test_pred = lr.predict(X_test)
# train_pred = lr.predict(X_train)

# train_mse = mean_squared_error(y_train, train_pred)
# test_mse = mean_squared_error(y_test, test_pred)
# print("train data set RMSE : ", round(train_mse ** 0.5, 3))
# print("test data set RMSE : ", round(test_mse ** 0.5, 3))

# 회귀분석 실습 2
# 공공 자전거 수요 예측 (Bike Sharing Demand)
# https://www.kaggle.com/c/bike-sharing-demand/overview

# 데이터 소개
# - 날짜 및 시간, 기온, 습도, 풍속 등의 정보를 기반으로 1시간 간격으로 자전거 대여 횟수를 기록한 데이터
# - 기록날짜는 2011년 1월 ~ 2012년 12월까지
# - 데이터에 자세한 정보는 소개된 캐글 사이트에서 확인 가능.

# Data Fields
# - datetime - hourly date + timestamp
# - season - 1 = spring, 2 = summer, 3 = fall, 4 = winter
# - holiday - whether the day is considered a holiday
# - workingday - whether the day is neither a weekend nor holiday
# - weather -
# - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
# - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
# - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
# - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
# - temp - temperature in Celsius
# - atemp - "feels like" temperature in Celsius
# - humidity - relative humidity
# - windspeed - wind speed
# - casual - number of non-registered user rentals initiated
# - registered - number of registered user rentals initiated
# - count - number of total rentals (Dependent Variable)

import calendar
import numpy as np
import pandas as pd
#from pandas.core.frame import DataFrame
#from pandas.core.series import Series #이렇게 불러도 됨.
import seaborn as sns # 통계적 plot
from scipy import stats #통계
import missingno as msno #결측치 보는 plot
from datetime import datetime #day
import matplotlib.pyplot as plt
import warnings #에러는 아닌데 주희하는게 뜨는것을 방지.
warnings.filterwarnings('ignore')

df_train = pd.read_csv('/content/drive/MyDrive/bike-sharing-demand/train.csv')
df_test = pd.read_csv('/content/drive/MyDrive/bike-sharing-demand/test.csv')

df_train.columns
df_test.columns
print(df_train.shape,df_test.shape)
df_train.describe()
df_train.info() # datetime : object
df_train['datetime'] #0번째 : 2011-01-01 00:00:00
df_train['date'] = df_train.datetime.apply(lambda x :x.split()[0])
df_train['Hour'] = df_train.datetime.apply(lambda x :x.split()[1].split(':')[0])
df_train["weekday"] = df_train.date.apply(lambda dateString : calendar.day_name[
    datetime.strptime(dateString,"%Y-%m-%d").weekday()])
df_train["month"] = df_train.date.apply(lambda dateString : calendar.month_name[
    datetime.strptime(dateString,"%Y-%m-%d").month])
df_train["season"] = df_train.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })
df_train["weather"] = df_train.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })

df_train.info()
categoryVariablesList = ['hour','weekday','month','season','weather','holiday','workingday']
for var in categoryVariablesList:
    df_train[var] = df_train[var].astype('category')
df_train.info()

# 결측치 확인
df_train.isna().sum()
# df_train.isnull().sum()

import missingno as msno # 결측치 보는 plot
msno.matrix(df_train, figsize = (12, 5)) # 결측치가 있다면 하얀색 줄이 그어짐

df_train_1 = df_train.copy() # 훼손방지
df_test_1 = df_test.copy()

df_train_1['datetime'] = pd.to_datetime(df_train_1['datetime'])

type(df_train_1)


# dataFrame 가능한 것
df_train_1['year'] = df_train_1['datetome'].dt.year
df_train_1['month'] = df_train_1['datetime'].dt.month
df_train_1['day'] = df_train_1['datetime'].dt.day
df_train_1['hour'] = df_train_1['datetime'].dt.hour
df_train_1['minute'] = df_train_1['datetime'].dt.minute
df_train_1['second'] = df_train_1['datetime'].dt.second
# 요일 데이터 - 일요일은 0
df_train_1['dayofweek'] = df_train_1['datetime'].dt.dayofweek