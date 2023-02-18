import requests
from bs4 import BeautifulSoup

headers ={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data =requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup =BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies =soup.select('#old_content >table>tbody>tr')

for movie in movies:
    # movie 안에 a 가 있으면,
    # (조건을 만족하는 첫 번째 요소, 없으면 None을 반환한다.)
     name_tag =movie.select_one('td.title>div>a')
#     point_tag =movie.select_one('td.point')
     if name_tag is not None:
        rank_tag =movie.select_one('td.ac>img')['alt']
        point_tag =movie.select_one('td.point')
        print(rank_tag,name_tag.text,point_tag.text)
# # print(movies[2].select_one('td.ac>img')['alt'])
    
# for movie in movies:
#     a = movie.select_one('td.title > div > a')
#     if a is not None:
#         title = a.text
#         rank = movie.select_one('td:nth-child(1) > img')['alt']
#         star = movie.select_one('td.point').text
#         print(rank,title,star)