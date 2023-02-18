from flask import Flask, render_template, jsonify, request

import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient 

app = Flask(__name__)

client = MongoClient('mongodb://namhuiju:skagmlwn95!@13.125.220.207', 27017)  
db = client.dbjungle 


@app.route('/')
def home():
    return render_template('index.html')

# POST 구현 
@app.route('/memo', methods=['POST'])
def post_memo():
    # # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']  # 클라이언트로부터 url을 받는 부분
    content_receive = request.form['content_give']  # 클라이언트로부터 comment를 받는 부분

    memo ={'title': title_receive, 'content':content_receive, 'like':0}
    # # 3. mongoDB에 데이터를 넣기
    db.memos.insert_one(memo)

    return jsonify({'result': 'success'})

# GET 구현
@app.route('/memo', methods=['GET'])
def read_memos():
    memos = list(db.memos.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'result': 'success', 'memos_list': memos})

@app.route('/delete', methods=['POST'])
def delete_memos():
    title_receive = request.form['title_give']
    db.memos.delete_one({'title': title_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})

@app.route('/like', methods=['POST'])
def like_memo():
    title_receive = request.form['title_give']
    memo = db.memos.find_one({'title': title_receive})
    
    new_like = memo['like'] + 1
    db.memos.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})

@app.route('/modify', methods=['POST'])
def modify_memo():
   
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)