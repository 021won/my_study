weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") # 비가 오나요? ture 출력
if weather == "비": # weather의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
    print("우산을 가져간다.")
elif weather == "맑음":
    print("날씨가 좋다.") # if문에서 False가 나왔기에 elif까지 올 수 있었음, if문이 True라면 elif까지 안옴
else: # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")
