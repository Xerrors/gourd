from flask import request, jsonify, abort, json, session
from app import app, db
from app.utils.articles import get_article_list_from_dirs, get_articles_from_db, scan_article_to_db, rename_markdown
from app.utils.articles import get_articles_from_zhihu, get_articles_from_csdn, parse_markdown
from app.utils.validate import validate_server_token
from app.utils.database import rtn_zones, get_all_messages
from app.config import DOMAIN_PRE


###
# 1. 博客动态相关
###


@app.route('/zones', methods=['GET'])
def get_zones():
    from app.tables import Zone
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
    from app.tables import Zone
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
    from app.tables import Zone
    msg = request.args.get('msg')
    status = request.args.get('status')
    db.session.add(Zone(msg=msg, status=status))
    db.session.commit()
    return jsonify({"data": rtn_zones()})


###
# 1. 博客动态相关
###


# 获取文章列表
@app.route('/articles', methods=["GET"])
def get_articles():
    source = request.args.get('source')
    if source == 'csdn':
        articles = get_articles_from_csdn()
    elif source == 'zhihu':
        articles = get_articles_from_zhihu()
    elif source == 'db':
        articles = get_articles_from_db()
    elif source == 'local':
        articles = get_article_list_from_dirs()
    else:
        return jsonify({"message": "没有该来源的文章~"}), 404
    return jsonify({"data": articles})


# TODO 仅用作测试使用
@app.route('/scan-article-to-db', methods=['GET'])
def scan_to_db():
    scan_article_to_db()
    articles = get_articles_from_db()
    return jsonify({"data": articles})


# TODO 数据验证，多次点击验证 IP
# 文章点赞功能
@app.route('/articles/like', methods=['POST'])
def add_like():
    from app.tables import LocalArticlesTable, Messages
    path = request.args.get('path')
    item = LocalArticlesTable.query.filter_by(path=path).first()
    if not item:
        abort(403, "你不对劲！")

    item.add_like()
    md = parse_markdown(item.local_path).metadata
    db.session.add(Messages(
        type="like",
        link=DOMAIN_PRE + path,
        content="有人点赞了你的文章《{}》".format(md['title'])
    ))
    db.session.commit()
    return jsonify({"message": "Good"})


# TODO 数据验证
# 文章评论功能
@app.route('/articles/comment', methods=['POST'])
def add_comment():
    from app.tables import LocalArticlesTable, LocalArticlesComment, Messages

    path = request.args.get('path')
    reviewer = request.args.get('reviewer')
    content = request.args.get('content')
    follow_id = request.args.get('follow_id')
    item = LocalArticlesTable.query.filter_by(path=path).first()

    if not item:
        abort(403, "你不对劲！")

    # 生成评论的消息
    md = parse_markdown(item.local_path).metadata
    if content:
        comment_msg = "网友“{}”评论了你的文章《{}》".format(reviewer, ['title'])
    else:
        comment_msg = "有人评论了你的文章《{}》".format(md['title'])

    db.session.add(LocalArticlesComment(path=path, reviewer=reviewer, content=content, follow_id=follow_id))
    db.session.add(Messages(
        type="comment",
        link=DOMAIN_PRE+path,
        content=comment_msg
    ))
    db.session.commit()
    return jsonify({"message": "Good"})


@app.route('/articles/md_source', methods=["POST"])
def upload_markdown():
    if not session.get('login'):
        return jsonify({"message": '登录之后再试~', 'code': 1001}), 403

    # 修改逻辑：对于已经存在的文章，应该发来该文章的 path，通过比对两次的 local 的 path
    # 是否相同，然后决定是否对目录下的文章进行扫描
    import frontmatter
    from app.tables import LocalArticlesTable

    md = request.get_data()
    with open('temp.md', 'wb+') as f:
        f.write(md)
    with open('temp.md', encoding='UTF-8') as f:
        md = frontmatter.load(f)

    if not md.get('title') or not md.get('date'):
        abort(404, '请上传符合博客文章要求的文章~')

    file_path = rename_markdown(md)
    path = request.args.get('path')
    item = LocalArticlesTable.query.filter_by(path=path).first()

    if not item or file_path != item.local_path:
        scan_article_to_db()

    # TODO: 后续需要添加自动编译提交的功能，但考虑到 vuepress 编译太慢了
    return jsonify({"message": "已经保存到{}".format(file_path)})


@app.route('/articles/md_source', methods=["GET"])
def get_markdown():
    from app.tables import LocalArticlesTable
    path = request.args.get('path')

    item = LocalArticlesTable.query.filter_by(path=path).first()

    if not item:
        scan_article_to_db()
        item = LocalArticlesTable.query.filter_by(path=path).first()

    if item:
        with open(item.local_path, encoding='UTF-8') as f:
            data = f.read()
            return jsonify({"data": data})
    else:
        abort(404, "不存在该文章！")


@app.route('/admin/login', methods=["POST"])
def admin_login():
    if session.get('login'):
        return jsonify({"message": '你已经登录过了~', "code": '1000'})

    data = request.get_data()
    data = json.loads(data)
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": '把所有空都填上~别落下~', "code": '1001'})

    if validate_server_token(username, password):
        from datetime import timedelta
        session.permanent =True
        app.permanent_session_lifetime =timedelta(minutes=60)#存活60分钟
        session['login'] = True
        return jsonify({"message": '登录成功~', "code": '1000'})
    else:
        return jsonify({"message": '你不对劲！', "code": '1001'})


@app.route('/admin/messages', methods=["GET"])
def get_messages():
    if not session.get('login'):
        abort(403, "登录之后再试~")

    source = request.args.get('source')
    if source == 'db':
        msgs = get_all_messages()
    else:
        msgs = []
    return jsonify({"data": msgs})


@app.route('/admin/logout', methods=["POST"])
def admin_logout():
    if session.get('login'):
        session.pop('login')
        return jsonify({"message": '退出成功~', "code": '1000'})
    else:
        return jsonify({"message": '还没登录，你不对劲~', "code": '1002'})


@app.route('/server/status', methods=["GET"])
def get_server_status():
    pass


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": str(e)}), 404


@app.errorhandler(403)
def page_not_found(e):
    return jsonify({"message": str(e)}), 403
