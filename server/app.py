# coding=utf-8
import os
import sys
from datetime import datetime

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_restful import fields, marshal_with, reqparse, Api, Resource, abort

from config import BLOG_PATH
from utils import get_article_list, get_articles_from_csdn, get_articles_from_zhihu

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config["Debug"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data', 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

# api = Api(app)
db = SQLAlchemy(app)


# class Zone(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime, default=datetime.now)
#     msg = db.Column(db.Text)
#     status = db.Column(db.String(20))

#     def to_json(self):
#         json_zone = {
#             'id': self.id,
#             'date': self.date,
#             'msg': self.msg,
#             'status': self.status
#         }
#         return json_zone


def rtn_zones():
    results = Zone.query.all()
    zones = [zone.to_json() for zone in results]
    return zones



@app.route('/zones', methods=['GET'])
def get_zones():
    id = request.args.get('id')
    if id:
        zone = Zone.query.get(id)
        if zone:
            return jsonify({"data": zone.to_json()})
        else:
            return jsonify({"message": "没有该动态~"}), 404
    else:
        return jsonify({"data": rtn_zones()})


@app.route('/zones', methods=['DELETE'])
def del_zone():
    id = request.args.get('id')
    if id:
        zone = Zone.query.get(id)
        if zone:
            db.session.delete(zone)
            db.session.commit()
            return jsonify({"message": "已删除"})
        else:
            return jsonify({"message": "没有该动态~"}), 404
    else:
        return jsonify({"message": "请提供删除的动态的 id"}), 403


@app.route('/zones', methods=["POST"])
def create_zone():
    msg = request.args.get('msg')
    status = request.args.get('status')
    zone = Zone(msg=msg, status=status)
    db.session.add(zone)
    db.session.commit()
    return jsonify({"data": rtn_zones()})


@app.route('/articles', methods=["GET"])
def get_articles():
    source = request.args.get('source')
    if source == 'csdn':
        articles = get_articles_from_csdn()
    elif source == 'zhihu':
        articles = get_articles_from_zhihu()
    else:
        articles = get_article_list()
    return jsonify({"data": articles})


@app.route('/server/status', methods=["GET"])
def get_server_status():
    from monitor.status import MachineStatus as MS
    pass


@app.route('/server/md_source', methods=["POST"])
def uploadMarkdown():
    import frontmatter
    md = request.get_data()
    with open('temp.md', 'wb+') as f:
        f.write(md)
    with open('temp.md', encoding='UTF-8') as f:
        md = frontmatter.load(f)
    
    if not md.get('title') or not md.get('date'):
        return jsonify({"message": "请上传符合博客文章要求的文章"}), 403

    # 解析文件名并根据分类保存到对应的文件目录下
    file_name = md['date'].strftime('%Y-%m-%d') + '-' + md['title'].replace(' ', '-') + '.md'
    if md.get('zhuanlan'):
        file_path = os.path.join(BLOG_PATH, md.get('zhuanlan'), file_name)
    elif type(md.get('categories')) == type([]):
        file_path = os.path.join(BLOG_PATH, md.get('categories')[0], file_name)
    elif type(md.get('categories')) == type(""):
        file_path = os.path.join(BLOG_PATH, md.get('categories'), file_name)
    else:
        file_path = os.path.join(BLOG_PATH, 'Others', file_name)

    os.renames('temp.md', file_path)

    # TODO: 后续需要添加自动编译提交的功能
    return jsonify({"message": "已经保存到{}".format(file_path)})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "This path can not be found!"}), 404


if __name__ == '__main__':
    from data.Tables import Zone
    app.run(debug=app.config["Debug"])
