# flask 시작 코드
# 통상적으로 flask 서버를 돌리는 파일은 app.py라고 이름 짓는다.
# Flask 서버를 만들 때는 항상 프로젝트 폴더 안에
# static, templates 폴더와 app.py를 먼저 만들고 시작해주세요!(기본구조)
# static 폴더는 HTML 파일 외에 이미지, css파일과 같은 파일을 담아두는 역할을 합니다.
# templates 폴더는 HTML 파일을 담아두고 불러오는 역할을 합니다.
# 폴더 안에 static, templates, app.py 를 만들고 폴더 오른쪽 클릭 후
# terminal 로 open 하고 가상환경을 만든다 (python3 -m venv .venv)
from flask import Flask, render_template
app = Flask(__name__)

# URL 별로 함수명이 같거나,
# route('/') 등의 주소가 같으면 안됩니다.


@app.route('/')
def home():
    # 페이지 창에 나온다.
    return render_template('index.html')


@app.route('/mypage')
def mypage():
    return 'This is My Page!'


if __name__ == '__main__':
    # http://localhost:5000/으로 접속했을떄
    app.run('0.0.0.0', port=5000, debug=True)
