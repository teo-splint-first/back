from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB : 27017 port
db = client.dbsplint


@app.route('/')
def home():
    return render_template('index.html')


# 템플릿 insert (API 역할)
@app.route('/write_template', methods=['POST'])
def write_template():
    title_receive = request.form['title_give']
    contents_receive = request.form['contents_give']

    template = {
        'title': title_receive,
        'contents': contents_receive
    }

    db.templates.insert_one(template)

    return jsonify({'result': 'success', 'msg': '템플릿 저장 성공'})


@app.route('/receive_template', methods=['GET'])
def read_reviews():
    # 1. url param로 넘어온 title값 받기
    title = request.args.get('title')
    # 2. DB에서 title = title 인 템플릿들 가져오기
    templates = list(db.templates.find({"title": title}))
    # 3. 성공 여부 & templates 반환하기
    return jsonify({'result': 'success', 'templates': templates})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

