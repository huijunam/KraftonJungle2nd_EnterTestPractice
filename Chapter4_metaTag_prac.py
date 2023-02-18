# 홈페이지 meta 태그 스크래핑 하기#
# requests 패키지 설치 명령어: python3 -m pip install requests
import requests #자바스크립트의 ajax 를 써서 GET요청 보냈던 것처럼 하기위해 파이썬에서는 requests패키지 이용한다.
from bs4 import BeautifulSoup #HTML 구조를 파악하는데 도움을 주는 beautifulsoup4 패키지

#스크래핑할 웹 주소 url
url ='https://platum.kr/archives/120958'

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data =requests.get(url, headers=headers)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup =BeautifulSoup(data.text, 'html.parser')
#select one 을 이용해 meta 태그의 property 속성이 "" 값인 값들 가져오기
og_image =soup.select_one('meta[property="og:image"]')
og_title =soup.select_one('meta[property="og:title"]')
og_description =soup.select_one('meta[property="og:description"]')

# print(og_image)
# print(og_title)
# print(og_description)

# content 출력
url_image =og_image['content']
url_title =og_title['content']
url_description =og_description['content']

print(url_image)
print(url_title)
print(url_description)

