import os
import frontmatter

from config import BLOG_PATH, CSDN_NAME


def get_article_list_from_dirs():
    assert os.path.exists(BLOG_PATH)
    article_list = []

    def extend_dir(path):
        for file in os.listdir(path):
            # 遍历所有文件
            markdown_path = os.path.join(path, file)

            # 如果是文件夹递归读取，否则读取文件
            if os.path.isdir(markdown_path):
                extend_dir(path=os.path.join(path, file))
            else:
                article_list.append(parse_markdown(markdown_path))

    extend_dir(BLOG_PATH)
    return article_list


def scan_article_to_db():
    from app import db
    from data.Tables import LocalArticlesTable
    assert os.path.exists(BLOG_PATH)
    article_list = []

    def extend_dir(path):
        for file in os.listdir(path):
            # 遍历所有文件
            markdown_path = os.path.join(path, file)

            # 如果是文件夹递归读取，否则读取文件
            if os.path.isdir(markdown_path):
                extend_dir(path=os.path.join(path, file))
            else:
                cur_frontmatter = parse_markdown(markdown_path)
                article = LocalArticlesTable.query.filter_by(path=cur_frontmatter['permalink']).first()
                if article:
                    article.front_matter = frontmatter.dumps(cur_frontmatter)
                    article.local_path = markdown_path
                    db.session.commit()
                else:
                    print(cur_frontmatter['permalink'], markdown_path, cur_frontmatter)
                    db.session.add(LocalArticlesTable(
                        path=cur_frontmatter['permalink'],
                        local_path=markdown_path,
                        front_matter=frontmatter.dumps(cur_frontmatter)
                    ))
                    db.session.commit()

    extend_dir(BLOG_PATH)
    return article_list


def get_articles_from_db():
    from data.Tables import LocalArticlesTable, LocalArticlesComment

    article_list = []
    query_result = LocalArticlesTable.query.all()

    for item in query_result:
        item_dict = {}
        item_dict['like_count'] = item.like_count
        item_dict['read_count'] = item.read_count
        item_dict.update(parse_markdown(item.local_path).metadata)
        item_dict['comment_count'] = LocalArticlesComment.query.filter_by(path=item.path).count()
        article_list.append(item_dict)

    return article_list


def parse_markdown(markdown_path):
    with open(markdown_path, encoding='UTF-8') as f:
        md = frontmatter.load(f)
        # 去除不规范的链接名称
        if md['permalink'][0] == '/':
            md['permalink'] = md['permalink'][1:]
        return md


def get_articles_from_csdn():
    """ 从数据库中找寻已经爬取的 CSDN 文章 """
    from data.Tables import CsdnArticlesTable, CsdnCount

    article_list = []
    query_result = CsdnArticlesTable.query.all()

    for item in query_result:
        item_dict = {}
        item_dict['title'] = item.title
        item_dict['date'] = item.create_date
        item_dict['article_id'] = item.article_id

        article_count = CsdnCount.query.filter_by(article_id=item.article_id).first()

        item_dict['read_count'] = article_count.read_count
        item_dict['comment_count'] = article_count.comment_count

        article_list.append(item_dict)

    return article_list


def get_articles_from_zhihu():
    return []


