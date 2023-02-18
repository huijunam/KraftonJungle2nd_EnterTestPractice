import requests #자바스크립트의 ajax 를 써서 GET요청 보냈던 것처럼 하기위해 파이썬에서는 requests패키지 이용
from bs4 import BeautifulSoup #HTML 구조를 파악하는데 도움을 주는 beautifulsoup4 패키지
from pymongo import MongoClient #pymongo 기본 셋팅 (1)
#pymongo 기본 셋팅 (2)
client =MongoClient('localhost', 27017)# mongoDB는 27017 포트로 돌아갑니다.
db =client.dbjungle # 'dbjungle'라는 이름의 db를 만듭니다.
##pymongo 기본 셋팅 끝

#BeautifulSoup 사용
# URL을 읽어서 HTML를 받아오고,
headers ={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#해당 링크는 크래핑할 주소
data =requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup =BeautifulSoup(data.text,'html.parser')

# select를 이용해서, tr들을 불러오기
movies =soup.select('#old_content>table>tbody>tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag =movie.select_one('td.title>div>a')
    if a_tag is not None:
        rank =movie.select_one('td.ac>img')['alt']# img 태그의 alt 속성값을 가져오기
        title =a_tag.text                         # a 태그 사이의 텍스트를 가져오기
        star =movie.select_one('td.point').text   # td 태그 사이의 텍스트를 가져오기
        # print(rank,title,star)
        #각 영화마다 도큐먼트 만들어 하나씩 insert 하기
        doc ={
            'rank' :rank,
            'title':title,
            'star' :star
        }
        #mongoDB movies 라는 collection에 데이터를 insert
        db.movies.insert_one(doc)