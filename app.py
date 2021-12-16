from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient
import random


app = Flask(__name__)

# client = MongoClient('localhost', 27017)  # mongoDB : 27017 port
# db = client.dbsplint

templates = [{"id": 0, "category": "huisic", "template": {"title": "출출한밤 야식", "list": [{"name": "치킨", "point": 5}, {"name": "치킨", "point": 5}, {"name": "치킨", "point": 5}, {"name": "치킨", "point": 5}]}},
            {"id": 1, "category": "boonsik", "template": {"title": "분식 최고", "list": [{"name": "김밥", "point": 5}, {"name": "쫄면", "point": 5}, {"name": "떡볶이", "point": 5}, {"name": "돈까스", "point": 5}]}},
            {"id": 2, "category": "japan", "template": {"title": "일본스러운 일식", "list": [{"name": "초밥", "point": 5}, {"name": "돈까스", "point": 5}, {"name": "규동", "point": 5}, {"name": "초밥", "point": 5}]}},
            {"id": 3, "category": "meat", "template": {"title": "고기고기고기", "list": [{"name": "삼겹살", "point": 5}, {"name": "등심", "point": 2}, {"name": "안심", "point": 5}, {"name": "소고기", "point": 5}]}},
             {"id": 4, "category": "huisic", "template": {"title": "출출한밤 야식", "list": [{"name": "치킨", "point": 10}, {"name": "치킨", "point": 2}, {"name": "치킨", "point": 6}, {"name": "치킨", "point": 8}]}},
             {"id": 5, "category": "boonsik", "template": {"title": "분식 최고", "list": [{"name": "김밥", "point": 10}, {"name": "쫄면", "point": 2}, {"name": "떡볶이", "point": 6}, {"name": "돈까스", "point": 8}]}},
             {"id": 6, "category": "japan", "template": {"title": "일본스러운 일식", "list": [{"name": "초밥", "point": 10}, {"name": "돈까스", "point": 2}, {"name": "규동", "point": 6}, {"name": "초밥", "point": 8}]}},
             {"id": 7, "category": "meat", "template": {"title": "고기고기고기", "list": [{"name": "삼겹살", "point": 10}, {"name": "등심", "point": 2}, {"name": "안심", "point": 6}, {"name": "소고기", "point": 8}]}},
             {"id": 8, "category": "huisic", "template": {"title": "출출한밤 야식", "list": [{"name": "치킨", "point": 8}, {"name": "치킨", "point": 5}, {"name": "치킨", "point": 5}, {"name": "치킨", "point": 3}]}},
            {"id": 9, "category": "boonsik", "template": {"title": "분식 최고", "list": [{"name": "김밥", "point": 8}, {"name": "쫄면", "point": 5}, {"name": "떡볶이", "point": 5}, {"name": "돈까스", "point": 3}]}},
            {"id": 10, "category": "japan", "template": {"title": "일본스러운 일식", "list": [{"name": "초밥", "point": 8}, {"name": "돈까스", "point": 5}, {"name": "규동", "point": 5}, {"name": "초밥", "point": 3}]}},
            {"id": 11, "category": "meat", "template": {"title": "고기고기고기", "list": [{"name": "삼겹살", "point": 8}, {"name": "등심", "point": 2}, {"name": "안심", "point": 5}, {"name": "소고기", "point": 3}]}},
             {"id": 12, "category": "huisic", "template": {"title": "출출한밤 야식", "list": [{"name": "치킨", "point": 2}, {"name": "치킨", "point": 2}, {"name": "치킨", "point": 1}, {"name": "치킨", "point": 3}]}},
             {"id": 13, "category": "boonsik", "template": {"title": "분식 최고", "list": [{"name": "김밥", "point": 2}, {"name": "쫄면", "point": 2}, {"name": "떡볶이", "point": 1}, {"name": "돈까스", "point": 2}]}},
             {"id": 14, "category": "japan", "template": {"title": "일본스러운 일식", "list": [{"name": "초밥", "point": 2}, {"name": "돈까스", "point": 2}, {"name": "규동", "point": 1}, {"name": "초밥", "point": 2}]}},
             {"id": 15, "category": "meat", "template": {"title": "고기고기고기", "list": [{"name": "삼겹살", "point": 2}, {"name": "등심", "point": 2}, {"name": "안심", "point": 1}, {"name": "소고기", "point": 2}]}}
             ]


# 템플릿 insert
@app.route('/create_template', methods=['POST'])
def create_template():
    title_receive = request.form['title_give']
    contents_receive = request.form['contents_give']
    template = {
        'id': len(templates) + 1,
        'title': title_receive,
        'contents': contents_receive
    }
    templates.append(template)

    return jsonify({'result': 'success', 'msg': '템플릿 저장 성공'})


# template list 보내기
@app.route('/receive_templates', methods=['GET'])
def read_templates():
    # 1. url param로 넘어온 title값 받기
    category = request.args.get('category')
    # 2. DB에서 title = title 인 템플릿들 가져오기
    return_templates = []
    for t in templates:
        if t['category'] == category:
            return_templates.append(t)
    # 3. 성공 여부 & templates 반환하기
    return jsonify({'result': 'success', 'templates': return_templates})


# id 값으로 최종 룰렛 돌릴 템플릿 결정 roulette
@app.route('/receive_roulette', methods=['GET'])
def read_roulette():
    # 1. url param 로 넘어온 id 값 받기
    _id = request.args.get('id')
    # 2. DB에서 id 값으로 해당하는 템플릿 가져오기
    return_template = []  # 모양 {title : "", list : [{name : "", point : 1}]}
    for t in templates:
        if t['id'] == _id:
            return_template.append(t['template'])
    # 3. 성공 여부 & template 반환하기
    return jsonify({'result': 'success', 'roulette': return_template})


# update 룰렛
@app.route('/update_roulette', methods=['POST'])
def update_roulette():
    #
    template_receive = request.form['template_give']
    id_receive = request.form['id']
    templates[id_receive]['template'] = template_receive


if __name__ == '__main__':
    app.run()
