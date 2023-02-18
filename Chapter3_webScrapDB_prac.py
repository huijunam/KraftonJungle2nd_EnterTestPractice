#pymongo 기본 코드 
from pymongo import MongoClient 
client =MongoClient('localhost',27017)# mongoDB는 27017 포트로 돌아갑니다.
db =client.dbjungle # 'dbjungle'라는 이름의 db를 만듭니다.
#-끝

#Q1. 영화제목 '매트릭스'의 평점을 가져오기
find_movie =db.movies.find_one({'title':'매트릭스'})
print(find_movie['star'])

#Q2. '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
find_same_star =db.movies.find({'star':find_movie['star']})
for same_star in find_same_star:
    print(same_star['title'])

#Q3. 매트릭스 영화의 평점을 0으로 만들기
#column 명 실수 주의!
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
# update_star =db.movies.find_one({'title':'매트릭스'})
# print(update_star['star'])
