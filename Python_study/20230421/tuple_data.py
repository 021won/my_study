# tuple(튜플)형
# 튜플은 element(요소)의 값이 정해지면 값을 수정할 수 없다.
# 삭제도 안됨
# 순서를 바꾸는 것도 값을 수정하는 부분이라 순서 변경 불가
# 인덱싱, 슬라이싱으로 꺼내도 튜플형이라 수정 불가
# mutable(변하는, 변하는 쉬운) / immutable(불변하는, 변하지 않는)
# mutable 수정 가능한 ex) list, dict
# immutable 수정 불가능 ex) int, float, str, tuple
# list와 tuple 사용 방식이 같지만 수정 가능 여부로 구분해서 사용

my_list = [1, 2, 3]
my_list[0] = 5
print(my_list)

my_tuple = (1, 2, 3)
my_tuple[0] = 5 # Error 튜플형은 수정 불가능
print(my_tuple) # 혹시라도 누가 수정하지않도록, 원본 보존

tuple_1 = ("Hello", "world", "python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))

t6 = tuple_1 + t2 # 새로운 값을 만들어 내는 것이기 때문에 +, * 연산 가능
t7 = t3 * 3
t7 = t3 * 4
#print(t7)
print(t3[2])
print(t3[0:2])
print(len(t3))
print(t5[2][1])

t8 = (5, 3, 1, 4, 2) # 튜플형 순서 못바꿈, 순서를 바꾸는 것도 값을 수정하는 것
for i in t8: 
    print(i) # 튜플 순서대로 출력, 정렬 불가, 문자열 마찬가지로 불가

