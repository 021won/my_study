# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 불러옴
"""
import 모듈이름
"""
import my_module
my_module.add(1, 2)
my_module.sub(1, 2)
"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import * # * : 전체, 모두 가져온다는 뜻
"""
from my_module import add, sub
add(1, 2)
sub(1, 2)

from my_module import *
add(1, 2)
sub(1, 2)

import my_module

from my_calculator import MyCalculator
my_calculator = MyCalculator()
my_calculator.div(10, 0)

class ZeroCalculator(MyCalculator):
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:    
            print(f"{n1} / {n2} = {n1/n2}")
zero_calculator = ZeroCalculator
zero_calculator.div(10, 0)