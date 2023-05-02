# 데이터 수집 단계

# 데이터 수집 -> 데이터 분석/처리 -> 인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용

# http (hypertext transfer protocol) : hypertext를 전송하는 약속
# - request(요청) - response(응답)
# - client(웹브라우저) - server
# html (hypertext markup language)
# - 웹사이트를 표현하기 위한 언어
# <html></html> / < > : 태그
# - 프로그램언어는 아님
# - html 파싱(parsing)

# import requests

# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status)
# print(html)

# http 상태 코드
# 200 : OK / 요청 성공
# 302 : 리다이렉트 / 다른 페이지로 바로 연결
# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음 / 주소 잘못 입력한 경우
# 405 : Method Not Allowed 접근 방법이 잘못됨
# 400번 대는 Error / 내가 잘못한 경우가 많음
# 500 : Internal Server Eroor 서버 에러 / 개발자 잘못
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리
# http://naver.com/?~~~~~~
# 쿼리 : 개개인이 검색한 것
# - 쿼리이름=값&쿼리이름=값&쿼리이름=값

# import requests
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# print(response.text)
# print(type(response.text))

# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# html은 그냥 글자라서 우리 사용하기 편하게 파싱해주는 것
# html 태그
# <태그이름 속성 = 속성값>내용</태그이름>
# <html><head></head><body></body></html>
from bs4 import BeautifulSoup
html = "<html><body>Hello</body><html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.body.text)
print(type(soup.body.text))

import requests
from bs4 import BeautifulSoup
search_url = "https://www.google.com/search?tbm=isch&q=" # 네이버는 셀레니움(selenium) 참고
keyword = "맥주"

url = search_url + keyword
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(soup.body.div) # 바디에 맨 앞에 있던 div 하나만 가져옴
print(soup.find('div')) # 또 첫번째 것만 나옴
print(soup.find_all('div')) # div 모두 찾아옴
print(soup.find_all('div')[4])

imgs = soup.find_all('img')
import os
folder_name = "imgs"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
for idx, img in enumerate(imgs[1:]):
    print(idx, "번째 이미지 저장")
    file_name = f"{keyword}_{idx}.jpg"
    file_path = os.path.join(folder_name, file_name)
    img_response = requests.get(img['src'])
    img_data =  img_response.content
    with open(file_path, "wb") as f: # wb : 2진수, 바이트 사용하겠다는 뜻.
        f.write(img_data)
    
# enumerate(이터러블)
# 값 앞에 번호(인덱스)가 나옴
li1 = ["김연아", "류현진", "손흥민"]
for idx, name in enumerate(li1):
    print(name)
(0, '김연아')
(1, '류현진')
(2, '손흥민') # 인덱스와 값 같이 나옴

# 네이버 IT/과학 뉴스 크롤링
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# headers={"User-Agent": "Mozilla/5.0"} --> 크롤링 방지 회피
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class': 'list_body'})
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})
for headline in headlines:
    print(headline.text.strip())

# 과제
# crawling_result 폴더의 headlines.txt 파일에 저장하기
import os
folder_name = "crawling_result"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
# for headline in headlines:
#     print(headline.text.strip())
#     with open("crawling_result/headline.txt", "a", encoding="utf-8") as f:
#         f.write(headline.text.strip())
#         f.write("\n")
article_response = requests.get(headline['href'])
aritcle_soup = BeautifulSoup(article_response.text, "html.parser")
article = aritcle_soup.find('div', attrs={"id": "dic_area"})
print(article.text)

