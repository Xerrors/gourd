import os
import frontmatter

from config import BLOG_PATH, CSDN_NAME

# def parse_md(arg, dirname, files):
#     for file in files:
#         markdown_path = os.path.join(dirname, file)
#         with open(markdown_path, encoding='UTF-8') as f:
#             md = frontmatter.load(f)
#             article_list.append(md.metadata['title'])


def get_article_list():
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
                with open(markdown_path, encoding='UTF-8') as f:
                    md = frontmatter.load(f)
                    md['path'] = markdown_path
                    article_list.append(md.metadata)

    extend_dir(BLOG_PATH)
    return article_list


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


