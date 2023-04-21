# 리스트(list) 자료형
# 여러개의 값을 변수 1개에 저장
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 1, 1, 1, 1, 1]
# ["Hello", "World", "Python"]
# [1, "Hello", 2, "WOW"]
# [1, 2, ["Hello", "World"]]
# []

li_1 = [1, 2, 3]
print(li_1[0])
print(li_1[1])
print(li_1[2])
print(li_1[-1])
print(li_1[0] + li_1[1])

# li_2 = [1, 2, 3, [4, 5, 6]]
# print(li_2[3][0])
# print(li_2[2:3])
# print(li_2[1:])
# print(li_2[:2])

# li_3 = [1, 2, 3, 4, 5]
# # 출력 결과가 [2, 3]이 되도록 만드세요.
# print(li_3[1:3])
# print(len(li_3))
# li_3[0] = 10
# print(li_3)

# li_4 = [1, 2, 3]
# li_4.append([1,2,3])
# print(li_4)

# li = [1, 2, 3]
# li.insert(1, 10)
# print(li)

# li = [1, 2, 3, 2]
# li.remove(10)
# print(li)

# li = [1, 2, 3, 4]
# a = li.pop()
# print(li)
# print(a)
# b = li.pop(1)
# print(b)

# li = [1, 2, 3]
# idx = li.index(10)
# print(idx)

# li = [5, 3, 1, 4, 2]
# li.sort()
# print(li)
# li.sort(reverse = True)
# print(li)

# li = [5, 1, 3, 4, 2]
# li.reverse()
# print(li)

# li = [1, 2, 3, 2]
# cnt = li.count(10)
# print(cnt)

# li_1 = [1, 2, 3]
# li_2 = [4, 5, 6]
# print(li_1 + li_2)
# a = li_1.extend(li_2)
# print(a)

# li =[1, 2, 3]
# print(li * 3)