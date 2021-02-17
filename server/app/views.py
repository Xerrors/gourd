from flask import request, jsonify, abort, json, session
from app import app, db
from app.utils.articles import get_article_list_from_dirs, get_articles_from_db, scan_article_to_db, rename_markdown
from app.utils.articles import get_articles_from_zhihu, get_articles_from_csdn, parse_markdown
from app.utils.validate import validate_server_token
from app.utils.database import rtn_zones, get_all_messages, get_page_view_by_path, rtn_friends
from app.config import DOMAIN_PRE, TOKEN
from datetime import datetime


@app.route("/visit", methods=["GET"])
def visit():
    path = request.args.get('path')

    if not path:
        abort(403, "有毛病吧！")

    from app.tables import PageViewTable
    db.session.add(PageViewTable(
        ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        path=path,
        user_agent=request.user_agent.browser,
    ))
    db.session.commit()

    count = get_page_view_by_path(request.args.get("count"))
    return jsonify({"message": "Welcome", "data": count})

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
    token = request.args.get('token')

    if token != TOKEN:
        abort(403, "Token 不对劲！")
    elif id:
        zone = Zone.query.get(id)
        if zone:
            db.session.delete(zone)
            db.session.commit()
            return jsonify({"message": "已删除", "data": rtn_zones()})
        else:
            return jsonify({"message": "没有该动态~"}), 404
    else:
        return jsonify({"message": "请提供删除的动态的 id"}), 403


@app.route('/zones', methods=["POST"])
def create_zone():
    from app.tables import Zone
    msg = request.args.get('msg')
    status = request.args.get('status')
    token = request.args.get('token')

    if token != TOKEN:
        abort(403, "Token 不对劲！")
    db.session.add(Zone(msg=msg, status=status, date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    db.session.commit()
    return jsonify({"data": rtn_zones()})


@app.route('/friends', methods=["GET"])
def get_friends():
    from app.tables import FriendsTable
    id = request.args.get('id')
    if id:
        friend = FriendsTable.query.get(id)
        if friend:
            return jsonify({"message": "ok", "data": friend.to_json()})
        else:
            return jsonify({"message": "没有该动态~"}), 404
    return jsonify({"data": rtn_friends()})


@app.route('/friends', methods=["POST"])
def add_friend():
    from app.tables import FriendsTable
    name = request.args.get("name")
    avatar = request.args.get("avatar")
    title = request.args.get("title")
    mail = request.args.get("mail")
    site = request.args.get("site")
    quote = request.args.get("quote")
    token = request.args.get('token')

    if token != TOKEN:
        abort(403, "Token 不对劲！")

    if not name or not site or not quote:
        abort(403, "信息不全~")
    
    db.session.add(FriendsTable(name=name, avatar=avatar, title=title, mail=mail, site=site, quote=quote))
    db.session.commit()
    return jsonify({"data": rtn_friends()})


@app.route('/friends', methods=['DELETE'])
def del_friend():
    from app.tables import FriendsTable
    id = request.args.get('id')
    token = request.args.get('token')

    if token != TOKEN:
        abort(403, "Token 不对劲！")
    elif id:
        friend = FriendsTable.query.get(id)
        if friend:
            db.session.delete(friend)
            db.session.commit()
            return jsonify({"message": "已删除", "data": rtn_friends()})
        else:
            return abort(403, "删除错误~")
    else:
        return abort(403, "请提供id")


@app.route('/zhuanlan', methods=["GET"])
def get_zhuanlan():
    from app.tables import ZhuanlanTable

    if request.args.get("name"):
        result = db.session.query(ZhuanlanTable).filter_by(name=request.args.get("name"))
        return jsonify({"message": "here", "data": result.to_json()})
    else:
        result = db.session.query(ZhuanlanTable).all()
        zhuanlans = [item.to_json() for item in result]

        return jsonify({"message": "here", "data": zhuanlans})


@app.route('/zhuanlan', methods=["POST"])
def add_zhuanlan():
    from app.tables import ZhuanlanTable
    



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
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        link=DOMAIN_PRE + path,
        content="有人点赞了你的文章《{}》".format(md['title'])
    ))
    db.session.commit()
    return jsonify({"message": "感谢支持~"})


# TODO 数据验证
# 文章评论功能
@app.route('/articles/comment', methods=['POST'])
def add_comment():
    from app.tables import LocalArticlesTable, LocalArticlesComment, Messages

    path = request.args.get('path')
    reviewer = request.args.get('reviewer')
    reviewer_mail = request.args.get('reviewer_mail')
    content = request.get_data()
    content = str(content, encoding = "utf-8")
    follow_id = request.args.get('follow_id')
    follow_name = request.args.get('follow_name')
    item = LocalArticlesTable.query.filter_by(path=path).first()

    if not item:
        abort(403, "你不对劲！")
    
    if len(content) == 0:
        return abort(403, "你不对劲~")

    # 生成评论的消息
    md = parse_markdown(item.local_path).metadata
    if reviewer:
        comment_msg = "网友“{}”评论了你的文章《{}》".format(reviewer, md['title'])
    else:
        comment_msg = "有人评论了你的文章《{}》".format(md['title'])

    db.session.add(LocalArticlesComment(
        path=path, 
        reviewer=reviewer,
        reviewer_mail=reviewer_mail,
        content=content,
        follow_id=follow_id,
        follow_name=follow_name,
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    ))
    db.session.add(Messages(
        type="comment",
        link=DOMAIN_PRE+path,
        content=comment_msg,
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    ))
    db.session.commit()
    return jsonify({"message": "Good"})


@app.route('/articles/comment', methods=['GET'])
def get_comments():
    path = request.args.get('path')
    if not path:
        abort(403, "你就是不对劲，搞事情啊~")
    
    from app.tables import LocalArticlesComment
    query_result = LocalArticlesComment.query.filter_by(path=path).all()
    comments = [result.to_json() for result in query_result]
    return jsonify({"message": "Good!", "data": comments}) 


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

    if not md.get('title') or not md.get('date') or not md.get('permalink'):
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


@app.route('/admin/readmessage', methods=["POST"])
def read_message():
    if not session.get('login'):
        abort(403, "登录之后再试~")

    from app.tables import Messages

    id = request.args.get('id')
    if not id:
        abort(404, "请提供id~")
    if id == 'all':
        msgs = Messages.query.all()
        for msg in msgs:
            msg.set_as_readed()
        db.session.commit()
    else:
        msg = Messages.query.get(id)
        if msg:
            msg.set_as_readed()
            db.session.commit()
        else:
            abort(403, "不存在该id")

    msgs = get_all_messages()
    return jsonify({"message": "Success", "data": msgs})


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
