# 거꾸로 배열해도 같은 단어 또는 문장이 되는 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True, 아니면 False를 반환하도록 정의하세요.
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False

def is_palindrome(input_string):
    # 기러기
    # 소주 만병만 주소
    # input_string = input_string.replace(" ", "") # 문자열 중간에 있는 공백 제거
    # length = len(input_string)
    # for i in range(length//2): # 회문이니 반만 검사하면 나머지 반은 따라옴
    #     if input_string[i] != input_string[length - 1 - i]:
    #         return False
    # return True    
    return input_string == input_string[::-1] # :: 역순 출력


result = is_palindrome("소주 만병만 주소")
print(result)

# reversed("안녕하세요.")
# join 넣어서 한번 해보기..!

# 코딩테스트
# SWEA
# 백준
# 프로그래머스