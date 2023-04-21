# dictionary (딕셔너리) 자료형
# key-value 형태
# key: value
# {"이름": "이름", "나이": 18, "점수": [80, 90, 100], 1: "ㅎㅎ"}
# person = {
#     "이름": "이름",
#     "나이": 18,
#     "점수": {
#         "영어": 80,
#         "국어": 90,
#         "수학": 100
#     }
# }
# print(person["나이"])
# print(person["점수"]["영어"])

# dict_1 = {1: 'a'}
# dict_1['b'] = 2 # 'b': 2 key-value 쌍 추가
# dict_1[1] = 'c'
# del dict_1[1]
# print(dict_1)

dict_2 = {1: 'a', 2: 'b', 3: 'c'}
# keys()
# 딕셔너리에서 key 값만 리스트 형태로 돌려준다
"""
dict_keys = dict_2.keys()
print(dict_keys)
"""
# 딕셔너리에서 value 값만 리스트 형태로 돌려준다
dict_value = dict_2.values()
print(dict_value)
# 딕셔너리에서 key-value  쌍을 튜플로 묶은 리스트 형태로 돌려준다
dict_items = dict_2.items()
print(dict_items)

# get(key값)
# key에 대응되는 value를 돌려준다
# key값이 존재하지 않으면 none을 돌려준다
# dict_2["나이"]
print(dict_2.get("나이", "나이 불명"))
# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
dict_2.clear()
print(dict_2)