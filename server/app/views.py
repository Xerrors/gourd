from flask import request, jsonify, abort
from app import app, db
from app.utils.articles import get_article_list_from_dirs, get_articles_from_db, scan_article_to_db, rename_markdown
from app.utils.articles import get_articles_from_zhihu, get_articles_from_csdn, rebuild
from app.utils.zone import rtn_zones


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
    from app.tables import LocalArticlesTable
    item = LocalArticlesTable.query.filter_by(path=request.args.get('path')).first()
    if item:
        item.add_like()
        db.session.commit()
        return jsonify({"message": "Good"})
    else:
        return jsonify({"message": "不存在"}), 404


# TODO 数据验证
# 文章评论功能
@app.route('/articles/comment', methods=['POST'])
def add_comment():
    from app.tables import LocalArticlesComment
    db.session.add(LocalArticlesComment(
        path=request.args.get('path'),
        reviewer=request.args.get('reviewer'),
        content=request.args.get('content')
    ))
    db.session.commit()
    return jsonify({"message": "Good"})


@app.route('/articles/md_source', methods=["POST"])
def uploadMarkdown():
    import frontmatter
    md = request.get_data()
    with open('temp.md', 'wb+') as f:
        f.write(md)
    with open('temp.md', encoding='UTF-8') as f:
        md = frontmatter.load(f)

    if not md.get('title') or not md.get('date'):
        return abort(404, '请上传符合博客文章要求的文章~')

    file_path = rename_markdown(md)
    scan_article_to_db()

    # TODO: 后续需要添加自动编译提交的功能
    return jsonify({"message": "已经保存到{}".format(file_path)})


@app.route('/articles/md_source', methods=["GET"])
def getMarkdown():
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
        return abort(404, "不存在该文章！")


@app.route('/server/status', methods=["GET"])
def get_server_status():
    pass


@app.route('/rebuild', methods=["GET"])
def get_rebuild():
    rebuild()
    return jsonify({"message": "Good Job!"})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": str(e)}), 404
